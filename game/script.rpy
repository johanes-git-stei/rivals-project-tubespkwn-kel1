# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



init python:
    def typing_noise(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/Text-blip.mp3")
        elif event == "slow_done":
            renpy.sound.stop()

define f = Character("Narrator", color = "#ffffff"  , callback=typing_noise)#color="#e96b8d"
define player = Character("[povname]", color = "#ffffff" , callback=typing_noise)#color="#17ddcd"
define b = Character("Barista", color = "#ffffff" , callback=typing_noise)#color="#cc30fb"
define k = Character("Kritikus", color = "#ffffff" , callback=typing_noise)#color="#d5f34f"
define p = Character("Petani Kopi",  color = "#ffffff" , callback=typing_noise)#color="#55e434ff"
# The game starts here.


label start:
    play music "audio/chill-chords-143504.mp3" volume 0.3
    scene coffeeshop_cashier

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    $ renpy.pause(2.00)
    f "Kamu adalah seorang manager dari sebuah barista"
    f "Hari ini adalah hari pertamamu bekerja!!!"

    f "Untuk saat ini, pilih penampilanmu"
menu : 
    "Laki-laki":
        jump choices1_a
    "Perempuan":
        jump choices1_b
label choices1_a:
    f "Baik, kamu memilih karaktermu sebagai laki-laki!"
    jump defineName
label choices1_b:
    f "Baik, kamu memilih karaktermu sebagai perempuan!"
    jump defineName
    
label defineName :
    $povname = renpy.input("Siapa namamu?").strip()
    if povname == "":
        "Nama harus berupa karakter!"
        jump defineName

    if not povname.isalpha() :
        "Nama tidak boleh berisikan Nomor ataupun Simbol!"
        jump defineName
        

    f "Halo [povname]!!"
    f "Kamu akan menjalani hari hari yang penuh dengan tantangan, dan kamu harus melewatinya dengan hati penuh semangat"
    stop music fadeout 1.0
    #disini harusnya scenenya tiba tiba berubah gitu jadi hitam atau mati, di fadeout
    jump ch01
    # Rifts apart/change bg i guess this should be, untuk sebelumnya ada lebih baiknya untuk
label ch01 :
    #Tokoh berdiri di depan pintu cofee shop
    #Show player angry/upset
    #Harusnya disini ada pause dulu bbrp detik
    play audio "audio/Surprised.mp3" volume 0.8
    show ceo at Position(xalign=0.1, yalign=0.57)
    player "Berani sekali orang itu menjual kopi di depan mata kita" 
    hide ceo
    show barista at Position(xalign = 0.9, yalign = 0.57)
    b "Sepertinya kita juga perlu untuk menjual produk kopi yang baru untuk menarik konsumen"
    hide barista
    show ceo at Position(xalign=0.1, yalign=0.57)
    player "Tapi, aku bermimpi orang orang bisa menyukai kopi otentik Indonesia"
    hide ceo
    show barista at Position(xalign = 0.9, yalign = 0.57)
    b "Lalu, mau sampai kapan engkau bermimpi? saingan kita udah ada di depan mata bos"
    hide barista
    show ceo at Position(xalign=0.1, yalign=0.57)
    player "Akan aku pikirkan terlebih dahulu"
    hide ceo fadeout 1.0

    scene workspace_infront_laptop
    f "Kamu melihat layar laptop dengan gelisah sambil menggerutu"
    #show player thinking/confuses with a cloud of thinking americano and luwak
    player "Hmmm, Pilih yang mana ya?"
    jump pilihkopi

label pilihkopi :
menu :
    "Tetap menjaga kopi luwak":
        scene coffeeshop_cashier        
        jump pilihkopi_A

    "Tetap menambahkan menu kopi baru":
        scene coffeeshop_cashier        
        jump pilihkopi_B

#========================================================BAB 1 END======================================================
label pilihkopi_A :

    player "Aku tetap ingin menjual kopi luwak otentik Indonesia. Kopi ini adalah identitas kita!"
    f "Beberapa hari kemudian..."
    #Show scene baru
    f "Seorang kritikus kopi terkenal datang ke coffee shop dan memesan kopi..."
    show barista at Position(xalign = 0.9, yalign = 0.57)
    b "Selamat datang, silahkan pak, ada yang bisa dibantu?"
    hide barista
    show kritikus at Position(xalign=0.1, yalign=0.57)
    k "Kopi apa yang direkomendasikan disini?"
    hide kritikus
    show barista at Position(xalign = 0.9, yalign = 0.57)
    b "Yang direkomendasikan disini adalah kopi luwak, Pak."
    b "Apakah bapak ingin mencicipi kopi luwak kami?"
    hide barista
    show kritikus at Position(xalign=0.1, yalign=0.57)
    k "Oke, saya akan pesan itu"
    hide kritikus
    #MINIGAME pembuatan kopi



    #Setelah minigame selesai 
    jump story1
label story1:
    f "Beberapa minggu kemudian..."

    f "Namun, tiba-tiba terjadi kekurangan pasokan biji kopi luwak akibat cuaca ekstrem di daerah penghasil kopi. "
    f "Kamu menghadapi dilema besar antara harus menaikkan harga kopi atau mencari alternatif pasokan sementara."
    #Delay
    f "Kamu berdiskusi dengan barista mengenai pilihan yang tersedia"
    show ceo at Position(xalign=0.1, yalign=0.57)
    player "Jika kita menaikkan harga, kita mungkin kehilangan pelanggan setia"
    player "Tapi jika kita mencari pasokan alternatif, kualitas kopi kita mungkin menurun"
    hide ceo
    show barista at Position(xalign = 0.9, yalign = 0.57)
    b "Ini memang situasi yang sulit, bos. Kita harus segera mengambil keputusan"
    hide barista
    jump tantangan
label tantangan:
menu : 
    "Naikkan harga kopi luwak.":     
        jump naikkan

    "Cari pasokan alternatif sementara":
        jump alternatif

label naikkan:
    scene coffeeshop_cashier  
    f "Kamu memutuskan untuk menaikkan harga kopi luwak dan memberikan penjelasan transparan kepada pelanggan tentang situasi yang menyebabkan keputusan tersebut."
    "Pelanggan1" "Kok harganya jadi naik drastis? Padahal rasa kopinya lebih cocok dengan harga sebelumnya loh"
    "Pelanggan2" "Tapi ini tetep worth it to buy kok!!! Coba aja buat kopinya sendiri, masa iya harus pelihara dan olah kotoran luwaknya sendiri?!"
    f "Beberapa pelanggan setia mengerti dan tetap mendukung coffee shop kamu, sementara yang lain berhenti datang karena harga yang terlalu tinggi."
    f "Namun, penjualan tetap stabil dan kamu berhasil mempertahankan kualitas kopi luwak."

label GoodEnd1 : 
    f "Setelah beberapa bulan, pasokan biji kopi luwak kembali normal, dan kamu menurunkan harga kembali."
    f "Coffee shop kamu kembali ramai, dan kamu merasa bangga karena berhasil menjaga kualitas dan otentisitas produk lokal."
    f "Waaah, toko kita ramai sekali!. Aku akan terjun langsung melayani pelanggan!"
    #Mini game lagi kopi buat pelanggan
    #harusnya dibuat script lagi disini, seperti player "Selamat menikmati kopi nya!"
    return
hide barista

label alternatif:
    scene kebun_kopi #harusnya 'scene kebun_kopi'
    f " Kamu mencari pasokan alternatif biji kopi dari daerah lain sementara menunggu pasokan biji kopi luwak kembali normal."
    show petani at Position(xalign = 0.9, yalign = 0.57)
    p "Ini rasa yang paling mirip sama kopi luwak, pak. Harganya pun lebih murah"
    hide petani

    #hide kebun kopi 
    jump choices2

label choices2:
menu : 
    "Ambil yang ini deh" :
        hide kebun_kopi
        jump choices2_1
    "Pilih menaikkan harga" :
        hide kebun_kopi
        jump naikkann  
    

label choices2_1 :
    scene meja_pelanggan
    "Pelanggan3" "Kenapa rasa kopinya berubah? Padahal saya lebih suka citarasa yang lama."
    "Pelanggan4" "Tapi rasanya tetap enak dan tidak jauh berbeda dengan kopi sebelumnya."
    f "Beberapa pelanggan kecewa dengan perubahan rasa, namun sebagian besar memahami situasi dan tetap mendukung coffee shop kamu."
    f "Penjualan mengalami sedikit penurunan, tapi masih cukup untuk bertahan."
    #hide meja_pelanggan
    jump goodendchalternatif

label goodendchalternatif:
    f "Setelah beberapa bulan, pasokan biji kopi luwak kembali normal."
    f "Kamu kembali menyajikan kopi luwak asli dan mengadakan promosi untuk menarik kembali pelanggan."
    f "Perlahan tapi pasti, coffee shop kamu kembali ramai dan kamu merasa bangga telah melewati tantangan ini."
    return


#=================================================PILIHAN KOPI B (AMERICANO)==============================================
label pilihkopi_B :
    show ceo at Position(xalign=0.1, yalign=0.57)
    player "Sepertinya kita harus mencoba menambahkan menu kopi baru untuk menarik lebih banyak pelanggan."
    hide ceo
    "Plot Twist" "Saat coffee shop mulai menawarkan kopi baru seperti americano, penjualan kopi luwak justru menurun drastis."
    "Plot Twist" "Pelanggan lebih tertarik dengan kopi baru yang lebih murah dan cepat."
    f "Beberapa minggu kemudian..."
    #Minigame Y/N memberikan kopi dari tempat barista ke pelanggan dan diperlihatkan bahwa kopi americano lebih banyak yg beli.
    f "Kamu mendapatkan laporan bahwa pendapatan mulai menurun meskipun jumlah pelanggan baru bertambah."
    f "Kamu mulai merasakan tekanan karena harus memenuhi target penjualan sekaligus mempertahankan kualitas kopi luwak."

label Tantangan2 : 
    f "Kamu menghadapi dilema besar. Apakah akan tetap fokus pada kopi baru yang lebih laris, atau kembali mempromosikan kopi luwak yang autentik namun lebih mahal?"
    f "Kamu berdiskusi dengan barista mengenai pilihan yang tersedia."
    show ceo at Position(xalign=0.1, yalign=0.57)
    player "Kita butuh strategi yang bisa menyeimbangkan antara menarik pelanggan baru dan mempertahankan keaslian kopi kita."
    hide ceo
    show barista at Position(xalign = 0.9, yalign = 0.57)
    b "Ini tidak mudah, Bos. Pelanggan saat ini lebih memilih kopi yang murah dan cepat saji."
    hide barista
    f "Sementara itu, seorang pemasok menawarkan biji kopi luwak dengan harga lebih murah namun kualitas lebih rendah. "
    f "Kamu menghadapi dilema tambahan: apakah akan menerima tawaran tersebut atau menolaknya demi menjaga kualitas."
    jump Tantangan2Choices

label Tantangan2Choices :
menu:
    "Terima tawaran pemasok untuk biji kopi luwak murah." :
        jump pemasokbijimurah
    "Tolak tawaran pemasok dan tetap dengan kualitas tinggi." :
        jump rejectpemasokbijimurah


label pemasokbijimurah :
    f "Kamu memutuskan untuk menerima tawaran pemasok dan mulai menggunakan biji kopi dengan kualitas rendah."
    f "Awalnya, penjualan kopi baru meningkat pesat dan pelanggan baru datang berbondong-bondong."
    f "Namun, perlahan-lahan, reputasi coffee shop kamu mulai menurun karena kualitas kopi yang semakin menurun."
    jump lanjutantantangan
label lanjutantantangan :
    f "Dalam beberapa bulan, pelanggan setia mulai mengeluh tentang rasa kopi yang tidak lagi sama. Kamu juga menerima banyak ulasan negatif di media sosial."
    "Pelanggan 5" "Rasa kopinya semakin berubah, dan tidak terasa otentik kopi luwak lagi"
    "Pelanggan 6" "Saya setuju, rasanya semakin memburuk"
    #scene latar baru
    show ceo at Position(xalign=0.1, yalign=0.57)
    player "Apa yang harus kita lakukan? Jika terus begini, kita bisa kehilangan semua pelanggan."
    hide ceo
    show barista at Position(xalign = 0.9, yalign = 0.57)
    b "Kita harus mengambil keputusan cepat, Bos. Kualitas adalah kunci kesuksesan kita."
    hide barista
    return

label rejectpemasokbijimurah:
    scene coffeeshop_cashier
    f "Mff scriptnya belum saya lanjutin untuk yang ini hehe"
    return





