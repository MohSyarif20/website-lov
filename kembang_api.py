import tkinter as tk
import random
import math

# Membuat jendela
root = tk.Tk()
root.title("🎆 Animasi Kembang Api")
root.geometry("900x600")
root.resizable(False, False)

# Canvas
canvas = tk.Canvas(
    root,
    width=900,
    height=600,
    bg="black"
)
canvas.pack()


# Menyimpan semua partikel
partikel = []


class Partikel:
    def __init__(self, x, y, warna):
        self.x = x
        self.y = y
        self.warna = warna

        # Arah gerakan acak
        sudut = random.uniform(0, math.pi * 2)
        kecepatan = random.uniform(2, 7)

        self.dx = math.cos(sudut) * kecepatan
        self.dy = math.sin(sudut) * kecepatan

        # Gravitasi
        self.gravitasi = 0.08

        # Ukuran
        self.ukuran = random.randint(2, 4)

        # Lama hidup
        self.hidup = random.randint(40, 80)

    def gerak(self):
        self.x += self.dx
        self.y += self.dy

        # Efek gravitasi
        self.dy += self.gravitasi

        # Mengurangi kehidupan partikel
        self.hidup -= 1

    def gambar(self):
        canvas.create_oval(
            self.x - self.ukuran,
            self.y - self.ukuran,
            self.x + self.ukuran,
            self.y + self.ukuran,
            fill=self.warna,
            outline=""
        )


def buat_kembang_api():
    # Posisi ledakan
    x = random.randint(150, 750)
    y = random.randint(100, 300)

    warna = random.choice([
        "red",
        "yellow",
        "cyan",
        "magenta",
        "orange",
        "lime",
        "white"
    ])

    # Membuat banyak partikel
    for i in range(80):
        partikel.append(
            Partikel(x, y, warna)
        )


def animasi():
    canvas.delete("all")

    # Membuat kembang api secara acak
    if random.random() < 0.04:
        buat_kembang_api()

    # Menggerakkan semua partikel
    for p in partikel[:]:

        p.gerak()
        p.gambar()

        # Hapus partikel yang sudah habis
        if p.hidup <= 0:
            partikel.remove(p)

    # Judul
    canvas.create_text(
        450,
        40,
        text="🎆 KEMBANG API 🎆",
        fill="white",
        font=("Arial", 28, "bold")
    )

    # Menjalankan animasi lagi
    root.after(30, animasi)


# Mulai animasi
animasi()

# Menjalankan program
root.mainloop()