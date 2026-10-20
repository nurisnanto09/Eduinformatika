/**
 * =========================================================================================
 * GOOGLE APPS SCRIPT (GAS) - BACKEND ASESMEN SISTEM OPERASI & LMS INFORMATIKA
 * =========================================================================================
 * 
 * Petunjuk Pemasangan:
 * 1. Buka Google Spreadsheet Anda (bisa spreadsheet yang sama dengan data siswa / presensi).
 * 2. Klik menu "Extensions" (Ekstensi) > "Apps Script".
 * 3. Hapus kode lama atau tambahkan fungsi di bawah ini ke dalam file "Code.gs".
 * 4. Klik "Deploy" (Terapkan) > "New deployment" (Penerapan baru).
 * 5. Pilih tipe "Web app" (Aplikasi web).
 * 6. Set "Execute as": "Me" (Saya / akun email Anda).
 * 7. Set "Who has access": "Anyone" (Siapa saja - PENTING agar siswa bisa kirim tanpa login Google).
 * 8. Klik "Deploy", izinkan akses keamanan ("Advanced" > "Go to ... (unsafe)").
 * 9. Salin URL Web App yang berakhiran "/exec", lalu tempelkan ke file asesmen_sistem_operasi.html pada variabel GAS_WEB_APP_URL.
 */

// =========================================================================================
// 1. FUNGSI POST (Menerima Pengiriman Jawaban Siswa & Presensi)
// =========================================================================================
function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000); // Mencegah race condition ketika banyak siswa submit bersamaan

  try {
    var contents = e.postData.contents;
    var data = JSON.parse(contents);
    var action = data.action;

    var ss = SpreadsheetApp.getActiveSpreadsheet();

    // AKSI 1: SUBMIT HASIL ASESMEN SISTEM OPERASI
    if (action === "submit_asesmen") {
      var sheetName = "Hasil_Asesmen";
      var sheet = ss.getSheetByName(sheetName);

      // Jika sheet "Hasil_Asesmen" belum ada, buat otomatis beserta headernya
      if (!sheet) {
        sheet = ss.insertSheet(sheetName);
        var headers = [
          "Timestamp",
          "Nama Siswa",
          "Kelas",
          "NIS / No",
          "Nilai (0-100)",
          "Jumlah Benar",
          "Jumlah Salah",
          "Durasi Pengerjaan",
          "Q1 (Definisi OS)",
          "Q2 (Lapisan Bawang)",
          "Q3 (Hubungan Komponen)",
          "Q4 (Contoh OS)",
          "Q5 (Sistem vs Aplikasi)",
          "Q6 (Pengelolaan Proses)",
          "Q7 (Pengelolaan Memori)",
          "Q8 (Perangkat & I/O)",
          "Q9 (Interaksi Pengguna)",
          "Q10 (Penyediaan Utilitas)"
        ];
        sheet.appendRow(headers);

        // Styling Header Row
        var headerRange = sheet.getRange(1, 1, 1, headers.length);
        headerRange.setBackground("#2563EB");
        headerRange.setFontColor("#FFFFFF");
        headerRange.setFontWeight("bold");
        headerRange.setHorizontalAlignment("center");
        sheet.setFrozenRows(1);
      }

      // Ambil rincian jawaban 1-10
      var jwb = data.jawaban || {};
      var q1 = jwb[1] || jwb["1"] || "-";
      var q2 = jwb[2] || jwb["2"] || "-";
      var q3 = jwb[3] || jwb["3"] || "-";
      var q4 = jwb[4] || jwb["4"] || "-";
      var q5 = jwb[5] || jwb["5"] || "-";
      var q6 = jwb[6] || jwb["6"] || "-";
      var q7 = jwb[7] || jwb["7"] || "-";
      var q8 = jwb[8] || jwb["8"] || "-";
      var q9 = jwb[9] || jwb["9"] || "-";
      var q10 = jwb[10] || jwb["10"] || "-";

      // Tambahkan baris baru hasil asesmen siswa
      sheet.appendRow([
        data.timestamp || new Date().toLocaleString("id-ID"),
        data.nama || "Anonim",
        data.kelas || "-",
        data.nis || "-",
        data.nilai || 0,
        data.benar || 0,
        data.salah || 0,
        data.durasi || "-",
        q1, q2, q3, q4, q5, q6, q7, q8, q9, q10
      ]);

      // Format kolom nilai agar rata tengah
      var lastRow = sheet.getLastRow();
      sheet.getRange(lastRow, 5, 1, 3).setHorizontalAlignment("center");

      return ContentService.createTextOutput(JSON.stringify({
        status: "success",
        message: "Hasil asesmen berhasil dicatat ke Google Sheets",
        nama: data.nama,
        nilai: data.nilai
      })).setMimeType(ContentService.MimeType.JSON);
    }

    // AKSI 2: SIMPAN PRESENSI (Kompatibel dengan LMS Bilik Komputasi index.html)
    else if (action === "simpan_presensi") {
      var presensiSheet = ss.getSheetByName("Presensi");
      if (!presensiSheet) {
        presensiSheet = ss.insertSheet("Presensi");
        presensiSheet.appendRow(["Tanggal", "No Absen", "Nama Lengkap", "Status Kehadiran", "Waktu Rekam"]);
        presensiSheet.getRange("A1:E1").setBackground("#10B981").setFontColor("#FFFFFF").setFontWeight("bold");
        presensiSheet.setFrozenRows(1);
      }

      var list = data.dataKehadiran || [];
      var tgl = data.tanggalFormatted || data.tanggal;
      var now = new Date().toLocaleString("id-ID");

      list.forEach(function(item) {
        presensiSheet.appendRow([
          tgl,
          item.no,
          item.nama,
          item.status,
          now
        ]);
      });

      return ContentService.createTextOutput(JSON.stringify({
        status: "success",
        message: "Data presensi berhasil disimpan"
      })).setMimeType(ContentService.MimeType.JSON);
    }

    // Aksi tidak dikenal
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: "Action tidak dikenal: " + action
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

// =========================================================================
// 2. FUNGSI GET (Mengambil Data Siswa atau Tes Status API)
// =========================================================================
function doGet(e) {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    
    // Cari sheet data siswa
    var sheetSiswa = ss.getSheetByName("Siswa") || ss.getSheetByName("Daftar_Siswa") || ss.getSheets()[0];
    
    if (sheetSiswa) {
      var data = sheetSiswa.getDataRange().getValues();
      var headers = data[0];
      var result = [];

      for (var i = 1; i < data.length; i++) {
        var row = data[i];
        if (row[0] === "" && row[1] === "") continue; // Lewati baris kosong
        var obj = {};
        for (var j = 0; j < headers.length; j++) {
          obj[headers[j]] = row[j];
        }
        result.push(obj);
      }

      return ContentService.createTextOutput(JSON.stringify({
        status: "success",
        total_data: result.length,
        data: result
      })).setMimeType(ContentService.MimeType.JSON);
    }

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      message: "API Google Apps Script Asesmen Aktif",
      timestamp: new Date()
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}
