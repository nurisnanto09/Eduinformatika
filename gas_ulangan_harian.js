/**
 * =========================================================================================
 * GOOGLE APPS SCRIPT (GAS) - BACKEND ULANGAN HARIAN INFORMATIKA
 * Bobot: Pilihan Ganda (70 Poin) + Esai (30 Poin) = Total 100 Poin
 * =========================================================================================
 * 
 * 📌 JAWABAN PERTANYAAN: "APAKAH PERLU MEMBUAT GAS BARU?"
 * 
 * JAWABAN:
 * 1. TIDAK PERLU membuat Google Spreadsheet baru! Anda BISA menggunakan Google Spreadsheet 
 *    yang sama dengan asesmen sebelumnya (atau presensi).
 * 2. TETAPI Anda PERLU menambahkan/memperbarui kodenya dengan skrip di bawah ini, karena
 *    ulangan harian ini memiliki struktur kolom baru: Nomor Absen, Kondisi Awal Siswa, 
 *    Nilai PG (bobot 70), Reaksi Emot Nilai, dan 3 Wadah Lembar Foto Esai (bobot 30).
 * 3. Skrip ini secara otomatis akan membuat TAB SHEET BARU bernama "Hasil_Ulhar_Informatika"
 *    di dalam Google Spreadsheet Anda tanpa mengganggu sheet asesmen lama.
 * 
 * -----------------------------------------------------------------------------------------
 * PETUNJUK PEMASANGAN / UPDATE (HANYA 2 MENIT):
 * 1. Buka Google Spreadsheet Anda.
 * 2. Klik menu "Extensions" (Ekstensi) > "Apps Script".
 * 3. Salin (copy) seluruh kode di bawah ini, lalu tempelkan (paste) ke dalam file "Code.gs".
 * 4. Klik tombol "Deploy" (Terapkan) > "Manage deployments" (Kelola penerapan) > Edit (ikon pensil),
 *    pilih "New version" (Versi baru), lalu klik "Deploy".
 *    (Atau klik "New deployment" jika membuat proyek script baru: Tipe "Web app", 
 *    "Execute as: Me", "Who has access: Anyone").
 * 5. Salin URL Web App yang berakhiran "/exec", lalu masukkan ke file ulangan_harian.html 
 *    pada variabel GAS_WEB_APP_URL atau melalui menu pengaturan di halaman ujian.
 * 
 * ✅ URL Web App Aktif Anda:
 *    https://script.google.com/macros/s/AKfycbyLQRe7B4zb4AFktOHxONI2qdxbtDQ66ksQELbBnFTTsNRf96ea10SPTEI01f_EkA4-/exec
 * =========================================================================================
 */

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(15000); // Mencegah race condition ketika banyak siswa submit bersamaan

  try {
    var contents = e.postData.contents;
    var data = JSON.parse(contents);
    var action = data.action;

    var ss = SpreadsheetApp.getActiveSpreadsheet();

    // AKSI 1: SUBMIT ULANGAN HARIAN INFORMATIKA
    if (action === "submit_ulangan_harian" || action === "submit_asesmen") {
      var sheetName = "Hasil_Ulhar_Informatika";
      var sheet = ss.getSheetByName(sheetName);

      // Jika sheet "Hasil_Ulhar_Informatika" belum ada, buat otomatis beserta header cantiknya
      if (!sheet) {
        sheet = ss.insertSheet(sheetName);
        var headers = [
          "Timestamp",
          "Nama Lengkap Siswa",
          "No. Absen",
          "Kondisi Awal",
          "Nilai PG (Maks 70)",
          "Jml Benar PG",
          "Reaksi Emot Nilai",
          "Nilai Esai (Maks 30)",
          "Total Nilai Akhir (100)",
          "Foto Esai 1 (Flowchart)",
          "Foto Esai 2 (Excel)",
          "Foto Esai 3 (IPO)",
          "Durasi",
          "Kode Verifikasi"
        ];
        sheet.appendRow(headers);

        // Format header agar rapi dan profesional
        var headerRange = sheet.getRange(1, 1, 1, headers.length);
        headerRange.setBackground("#107c41"); // Hijau khas Excel
        headerRange.setFontColor("#ffffff");
        headerRange.setFontWeight("bold");
        headerRange.setHorizontalAlignment("center");
        sheet.setFrozenRows(1);
      }

      var nextRow = sheet.getLastRow() + 1;

      // Formula otomatis untuk menghitung Total Nilai (Kolom E + Kolom H)
      var formulaTotal = "=E" + nextRow + " + IF(ISBLANK(H" + nextRow + "), 0, H" + nextRow + ")";

      var rowData = [
        data.timestamp || new Date().toLocaleString('id-ID', { timeZone: 'Asia/Jakarta' }),
        data.nama || "-",
        data.absen || "-",
        data.kondisi_awal || "-",
        data.nilai_pg !== undefined ? data.nilai_pg : 0,
        data.benar_pg !== undefined ? data.benar_pg : 0,
        data.reaksi_nilai || "-",
        "", // Kolom Nilai Esai dikosongkan untuk diinput guru saat mengoreksi (Maks 30)
        formulaTotal, // Total Nilai Akhir dihitung otomatis oleh spreadsheet!
        data.foto_esai_1 ? "✅ Terunggah" : "❌ Kosong",
        data.foto_esai_2 ? "✅ Terunggah" : "❌ Kosong",
        data.foto_esai_3 ? "✅ Terunggah" : "❌ Kosong",
        data.durasi || "-",
        data.kode_verifikasi || "-"
      ];

      sheet.appendRow(rowData);

      // Rata tengah kolom-kolom numerik & status
      sheet.getRange(nextRow, 3).setHorizontalAlignment("center"); // Absen
      sheet.getRange(nextRow, 5, 1, 5).setHorizontalAlignment("center"); // Nilai & Status
      sheet.getRange(nextRow, 10, 1, 5).setHorizontalAlignment("center");

      return ContentService.createTextOutput(JSON.stringify({
        status: "success",
        message: "Data Ulangan Harian berhasil disimpan ke sheet " + sheetName,
        row: nextRow
      })).setMimeType(ContentService.MimeType.JSON);
    }

    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: "Action tidak dikenali"
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: err.toString()
    })).setMimeType(ContentService.MimeType.JSON);

  } finally {
    lock.releaseLock();
  }
}

// =========================================================================================
// 2. FUNGSI GET (Test status koneksi Google Apps Script)
// =========================================================================================
function doGet(e) {
  return ContentService.createTextOutput(JSON.stringify({
    status: "active",
    app: "Backend Ulangan Harian Informatika",
    timestamp: new Date().toISOString()
  })).setMimeType(ContentService.MimeType.JSON);
}


/**
 * 🛠️ FUNGSI INTI / TES LANGSUNG DARI GOOGLE APPS SCRIPT
 * Jika Anda ingin membuat Tab Sheet "Hasil_Ulhar_Informatika" secara instan sekarang juga
 * tanpa menunggu siswa submit, pilih fungsi "inisialisasiSheetManual" di toolbar atas lalu klik "Jalankan / Run".
 */
function inisialisasiSheetManual() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheetName = "Hasil_Ulhar_Informatika";
  var sheet = ss.getSheetByName(sheetName);

  if (!sheet) {
    sheet = ss.insertSheet(sheetName);
    var headers = [
      "Timestamp",
      "Nama Lengkap Siswa",
      "No. Absen",
      "Kondisi Awal",
      "Nilai PG (Maks 70)",
      "Jml Benar PG",
      "Reaksi Emot Nilai",
      "Nilai Esai (Maks 30)",
      "Total Nilai Akhir (100)",
      "Foto Esai 1 (Flowchart)",
      "Foto Esai 2 (Excel)",
      "Foto Esai 3 (IPO)",
      "Durasi",
      "Kode Verifikasi"
    ];
    sheet.appendRow(headers);

    var headerRange = sheet.getRange(1, 1, 1, headers.length);
    headerRange.setBackground("#107c41"); // Hijau Excel
    headerRange.setFontColor("#ffffff");
    headerRange.setFontWeight("bold");
    headerRange.setHorizontalAlignment("center");
    sheet.setFrozenRows(1);
    
    Logger.log("✅ Tab Sheet 'Hasil_Ulhar_Informatika' berhasil dibuat!");
  } else {
    Logger.log("ℹ️ Tab Sheet 'Hasil_Ulhar_Informatika' sudah ada.");
  }
}
