import requests
from bs4 import BeautifulSoup

def ekstraksi_data():
    """

    waktu           : 9:00 WIB
    cuaca           :Hujan Ringan
    Temperatur      :25°C
    Kelembapan      :90 %
    Kekuatan angin  :10 km/jam
    Arah Angin      : Timur
    """
#menghindari error menjadi None

    try:
        content = requests.get('https://www.bmkg.go.id/cuaca/prakiraan-cuaca.bmkg?Kota=Temanggung&AreaID=501268&Prov=11')
    except Exception:
        return None

# Mencari  waktu class sudah jelas
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        resulttime = soup.find('h2',{'class' : 'kota'})
        waktu = resulttime.text
# mencari tanggal
        resulttanggal = soup.find('div',{'class' : 'topbar-time hari-digit hidden-xs'})
        tanggal = resulttanggal.text
#mencari cuaca
        resultcuaca= soup.find('div', {'class': "kiri"})
        cuaca = resultcuaca.text
#mencari suhu
        resultsuhu= soup.find('h2', {'class': "heading-md"})
        suhu = resultsuhu.text
# mencari kelembapan
        resultKelembapan = soup.find('div', {'class' :"kanan"})
        resultp = resultKelembapan.findChildren('p')
        i = 1
        Kelembapan = None
        kekuatan = None

        for res in resultp:

            if i == 1:
                kelembapan = res.text
            if i == 2:
                kekuatan = res.text
                kekuatan1 = kekuatan[0:9]
                kekuatan2 = kekuatan[9:14]





            i = i + 1




#mencari hasil
        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['cuaca'] = cuaca
        hasil['suhu'] = suhu
        hasil['kelembapan'] = kelembapan
        hasil['kekuatan'] = kekuatan1
        hasil['arah'] = kekuatan2


        return hasil
    else :
        return None
#mencetak hasil
def tampilkan_data(result):
    if result is None:
        print('data tidak di temukan')
        return
    print(f"tanggal : {result['tanggal']}")
    print(f"1.waktu : {result['waktu']}")
    print(f"2.cuaca :{result['cuaca']}")
    print(f"3.suhu :{result['suhu']}")
    print(f"4.kelembapan :{result['kelembapan']}")
    print(f"5.kekuatan angin :{result['kekuatan']}")
    print(f"6.arah angin :{result['arah']}")

if __name__ == '__main__' :
    print('Aplikasi Cuaca di Temanggung')
    result = ekstraksi_data()
    tampilkan_data(result)
    print('thanks')


