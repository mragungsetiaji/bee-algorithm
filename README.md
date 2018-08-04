# Bee Algorithm

Tujuan dari kawanan lebah adalah untuk menemukan suatu area dengan kepadatan bunga tertinggi. Tanpa adanya pertikaian antara lebah tentang area mana yang akan dituju, mulailah pencarian bunga dari posisi acak dengan vektor kecepatan acak. Setiap lebah dapat mengingat posisi di mana jumlah maksimal quantity bunga ditemukan dan tahu di mana lebah lain menemukan maksimal kepadatan bunga. Ketika lebah memilih di antara tempat di mana ia menemukan jumlah maksimum bunga dan tempat yang dilaporkan oleh orang lain, lebah bergegas ke arah antara dua titik ini dan menghendaki antara ingatan pribadi dan refleks sosial. 

Dalam perjalanannya, lebah dapat menemukan tempat dengan konsentrasi bunga yang lebih tinggi daripada yang ditemukan sebelumnya. Di waktu setelahnya tempat ini dapat ditandai sebagai tempat dengan konsentrasi bunga tertinggi yang ditemukan oleh kawanan. Setelah itu seluruh kawanan akan bergegas ke arah tempat ini, mengingat meskipun pengamatan mereka sendiri. Jadi, lebah melakukan penelitian di lapangan dengan terbang ke tempat dengan konsentrasi bunga tertinggi. Mereka juga terus menerus membandingkan tempat-tempat yang mereka terbangi dengan yang ditemukan sebelumnya untuk menemukan konsentrasi bunga mutlak. Pada akhirnya, seekor lebah mengakhiri penerbangannya di tempat dengan konsentrasi bunga maksimum. Segera seluruh kawanan akan mencari di sekitar tempat itu.


## Mathematical model

Dalam Algoritma Lebah, koloni ini terdiri dari tiga kelompok lebah: lebah yang bekerja, penonton dan pengintai. Pengintai melakukan pencarian acak, lebah bekerja mengumpulkan makanan yang ditemukan sebelumnya dan penonton menonton pergerakan lebah yang bekerja dan memilih sumber makanan tergantung pada pergerakannya. Penonton dan pengintai disebut lebah yang tidak bekerja. Komunikasi antara lebah didasarkan pada pergerakan. Sebelum lebah mulai mengumpulkan makanan, mereka menyaksikan pergerakan lebah lain. Pergerakan tersebut adalah cara lebah menggambarkan dimana makanan berada.

Lebah yang bekerja dan tidak bekerja mencari sumber makanan di dekat sarang mereka. Seekor lebah pekerja menyimpan informasi tentang sumber makanan dan membagikannya dengan para penonton. Lebah pekerja yang solusinya tidak dapat ditingkatkan setelah sejumlah upaya yang pasti menjadi pengintai dan solusi mereka tidak digunakan setelah itu. Jumlah sumber makanan mewakili sumber solusi dalam populasi. Posisi sumber makanan merupakan solusi yang mungkin untuk masalah optimasi dan jumlah nektar dari sumber makanan sesuai dengan kualitas (kebugaran) dari solusi yang terkait.

## Algorithm
```
BEGIN
Initialize the population
Find current best agent for the initial iteration
Calculate the number of scouts, onlookers and employed bees
SET global best to current best
FOR iterator = 0 : iteration
  evaluate fitness for each agent
  sort fitness in ascending order and get best agents
  from best agents list select agents from a to c
  Create new bees which will fly to the best solution
  Evaluate current best agent
  IF function(current best) < function (global best)
    global best = current best
  END IF
END FOR
Save global best
```
## Arguments
Method aba hanya bisa argument standard

## Method invocation
method dapat dipanggil dengan meneruskan argumen dalam urutan berikut:

```
SwarmPackagePy.aba(n, function, lb, ub, dimension, iteration)
```