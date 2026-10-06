// Membuat love yang bergerak dari bawah ke atas

function buatLove() {

    const love = document.createElement("div");

    love.innerHTML = "❤️";

    love.className = "love-kecil";

    // Posisi horizontal acak
    love.style.left =
        Math.random() * 100 + "vw";

    // Ukuran acak
    love.style.fontSize =
        (15 + Math.random() * 35) + "px";

    // Kecepatan acak
    love.style.animationDuration =
        (3 + Math.random() * 5) + "s";

    document.body.appendChild(love);

    // Hapus setelah selesai
    setTimeout(() => {
        love.remove();
    }, 8000);
}


// Membuat love setiap 300 ms

setInterval(buatLove, 300);


// Tombol

function pesanLove() {

    document.getElementById("pesan").innerHTML =
        "❤️ Aku sayang kamu ❤️";

}