import pygame
import sys
import random
import math

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
lebar, tinggi = 800, 600
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption("Project Be")

# Warna
warna_langit = (135, 206, 235)  # biru langit
warna_rumput = (0, 128, 0)  # hijau rumput
warna_rumah = (255, 0, 0)  # merah rumah
warna_jendela = (135, 206, 250)  # biru jendela
warna_pintu = (160, 82, 45)  # coklat pintu
warna_awan = (255, 255, 255)  # putih awan
warna_matahari = (255, 165, 0)  # oranye matahari
warna_gunung = (139, 69, 19)  # coklat gunung

# Koordinat rumah
x_rumah, y_rumah = 300, 400  # Sesuaikan koordinat y agar sejajar dengan rumput

# Ukuran rumah
lebar_rumah, tinggi_rumah = 200, 150

# Ukuran jendela
lebar_jendela, tinggi_jendela = 40, 40

# Ukuran pintu
lebar_pintu, tinggi_pintu = 60, 100

# Variabel awan
awan = [
    {
        "x": random.randint(0, lebar),
        "y": random.randint(50, 200),
        "size": random.randint(20, 40),
    }
    for _ in range(3)
]
kecepatan_awan = 2

# Koordinat matahari
radius_matahari = 30  # Mengurangi nilai radius untuk membuat matahari lebih kecil
# faktor_skala_matahari = 1.0  # Faktor skala untuk matahari

x_matahari, y_matahari = (
    lebar // 2,
    tinggi // 4,
)  # Letakkan matahari sedikit lebih tinggi

# Koordinat gunung
ketinggian_gunung = [tinggi - 200, tinggi - 300, tinggi - 250]

jam = pygame.time.Clock()

# Loop utama
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Di dalam loop utama sebelum Gambar awan, tambahkan kode berikut:
    warna_awan = (
        max(200, min(warna_awan[0] + random.randint(-5, 5), 255)),
        max(200, min(warna_awan[1] + random.randint(-5, 5), 255)),
        max(200, min(warna_awan[2] + random.randint(-5, 5), 255)),
    )

    # Hapus layar
    layar.fill(warna_langit)

    # Gambar gunung
    pygame.draw.polygon(
        layar,
        warna_gunung,
        [
            (0, ketinggian_gunung[0]),
            (lebar / 4, ketinggian_gunung[1]),
            (lebar / 2, ketinggian_gunung[0]),
            (3 * lebar / 4, ketinggian_gunung[1]),
            (lebar, ketinggian_gunung[0]),
            (lebar, tinggi),
            (0, tinggi),
        ],
    )

    pygame.draw.polygon(
        layar,
        warna_gunung,
        [
            (0, ketinggian_gunung[1]),
            (lebar / 4, ketinggian_gunung[2]),
            (lebar / 2, ketinggian_gunung[1]),
            (3 * lebar / 4, ketinggian_gunung[2]),
            (lebar, ketinggian_gunung[1]),
            (lebar, tinggi),
            (0, tinggi),
        ],
    )

    pygame.draw.polygon(
        layar,
        warna_gunung,
        [
            (0, ketinggian_gunung[2]),
            (lebar / 4, tinggi),
            (lebar / 2, ketinggian_gunung[2]),
            (3 * lebar / 4, tinggi),
            (lebar, ketinggian_gunung[2]),
            (lebar, tinggi),
            (0, tinggi),
        ],
    )

    # Gambar rumput
    pygame.draw.rect(layar, warna_rumput, (0, tinggi - 50, lebar, 50))

    # Gambar rumah
    pygame.draw.rect(layar, warna_rumah, (x_rumah, y_rumah, lebar_rumah, tinggi_rumah))

    # Gambar atap
    pygame.draw.polygon(
        layar,
        (0, 0, 0),
        [
            (x_rumah, y_rumah),
            (x_rumah + lebar_rumah / 2, y_rumah - tinggi_rumah / 2),
            (x_rumah + lebar_rumah, y_rumah),
        ],
    )

    # Gambar jendela
    pygame.draw.rect(
        layar,
        warna_jendela,
        (x_rumah + 30, y_rumah + 30, lebar_jendela, tinggi_jendela),
    )

    # Gambar pintu
    pygame.draw.rect(
        layar,
        warna_pintu,
        (
            x_rumah + lebar_rumah - lebar_pintu - 30,
            y_rumah + 50,
            lebar_pintu,
            tinggi_pintu,
        ),
    )

    # Gambar awan
    for awn in awan:
        pygame.draw.circle(layar, warna_awan, (awn["x"], awn["y"]), awn["size"])

        # # Gerakkan awan dan tambahkan translasi pada koordinat y awan
        # awn["x"] += kecepatan_awan
        # if awn["x"] > lebar:
        #     awn["x"] = 0

    # Gambar matahari berbentuk lingkaran tanpa scaling
    pygame.draw.circle(layar, warna_matahari, (x_matahari, y_matahari), radius_matahari)

    # Tambahkan garis sinar matahari
    for i in range(12):
        sudut = math.radians(i * (360 / 12))
        pos_awal = (
            x_matahari + int(radius_matahari * 1.5 * math.cos(sudut)),
            y_matahari + int(radius_matahari * 1.5 * math.sin(sudut)),
        )
        pos_akhir = (
            x_matahari + int(radius_matahari * 2 * math.cos(sudut)),
            y_matahari + int(radius_matahari * 2 * math.sin(sudut)),
        )
        pygame.draw.line(layar, warna_matahari, pos_awal, pos_akhir, 2)

    # Perbarui tampilan
    pygame.display.flip()

    # Batasi kecepatan animasi
    jam.tick(30)
