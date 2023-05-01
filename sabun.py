import streamlit as st

st.subheader('Hallo, Selamat Datang di Smart Soap APP')
st.title('__**APLIKASI PENENTUAN KUALITAS SABUN MANDI CAIR**__')


st.write("---")
left_column, middle_column, right_column= st.columns(3)
with left_column:
    st.write('__**INTRO**__ - Sebuah aplikasi yang bertujuan untuk memudahkan pengguna agar dapat mengetahui kualitas __**sabun mandi cair**__ dengan mudah.')
with middle_column:
    st.write('''Aplikasi ini dibuat oleh kelompok 12:
1. Fatiha Syifa Giftari (2118859)
2. Fauziah Roihana Sinaga (2118862)
3. Marsha Zahra Nissa (2118906)
4. Rasty Silvia (2118965)
5. Wahyuni Zara Lubis (2119009)
''')

with right_column:
    st.write('Aplikasi ini mengacu pada __**SNI 06-4085-1996 tentang Sabun Mandi Cair**__.')
    st.write('Parameter yang digunakan yaitu, pengukuran pH dan penentuan kadar alkali bebas.')
    st.write('[Click here to view >](https://drive.google.com/file/d/1bmZgvRTgwqfmQcqfv4rx3jK1S0OBDSOG/view?usp=share_link)')

st.write("---")
import streamlit as st
st.markdown('__**INPUT DATA ANALISA**__')
st.caption('pengukuran pH sabun mandi cair dengan pH meter')
digit=3
ph1=st.number_input('Masukkan pH sabun mandi cair 1:')
ph2=st.number_input('Masukkan pH sabun mandi cair 2:')

st.write("---")
st.caption('pengukuran alkali bebas dengan metode asidimetri')
digit=4
bs=st.number_input('Masukkan bobot sampel (gram):',format='%.'+str(digit)+'f')
vb=st.number_input('Masukkan volume titran (mL):')
nb=st.number_input('Masukkan Konsentrasi NaOH (N):',format='%.'+str(digit)+'f')


st.write("---")
tombol=st.button('TAMPILKAN HASIL ANALISA [PENGUKURAN pH & ALKALI BEBAS]')
sim=st.button('TAMPILKAN KESIMPULAN')

if tombol:
    rerata=((ph1)+(ph2))/2
    RPD=((ph1)-(ph2))/rerata
    
    alkali=((vb)*(nb)*(40/1000))/(bs)
    
    st.success(f'Nilai rata - rata pH dari sabun mandi cair adalah {rerata}')
    if 8<rerata<11:
        reratax=st.write('Memenuhi syarat keberterimaan')
    elif 11<rerata<8:
        rerataxn=st.write('Tidak memenuhi syarat keberterimaan')
    
    st.success(f'Nilai %RPD yang diperoleh adalah {RPD}')
    if RPD<5:
        RPDx=st.write('Memenuhi syarat keberterimaan')
    elif RPD>=5:
        RPDxn=st.write('Tidak memenuhi syarat keberterimaan')
        
    st.success(f'Nilai kadar alkali bebas yang diperoleh adalah {alkali} %')
    if alkali<(1/10):
        alkalix=st.write('Memenuhi syarat keberterimaan')
    elif alkali>(1/10):
        alkalixn=st.write('Tidak memenuhi syarat keberterimaan')

if sim:
    rerata=((ph1)+(ph2))/2
    RPD=((ph1)-(ph2))/rerata
    
    alkali=((vb)*(nb)*(40/1000))/(bs)
    if 8<rerata<11 and RPD<5 and alkali<(1/10):
        st.write('__**KESIMPULAN ANALISA**__')
        st.write('Pada Analisa Sabun Mandi Cair dengan 2 parameter yaitu pengukuran pH dan penentuan kadar alkali bebas diperoleh hasil:')
        st.write('Rata - rata hasil pengukuran pH',rerata,'dinyatakan memenuhi syarat keberterimaan')
        st.write('%RPD dari pengukuran pH',RPD,'memenuhi syarat maka analisa dinyatakan baik')
        st.write('Kadar alkali bebas',alkali,'dinyatakan memenuhi syarat keberterimaan')
        st.write('Maka dapat disimpulkan bahwa Sabun Mandi Cair layak digunakan.')
        
    else:
        st.write('__**KESIMPULAN ANALISA**__')
        st.write('Pada Analisa Sabun Mandi Cair dengan 2 parameter yaitu pengukuran pH dan penentuan kadar alkali bebas diperoleh hasil:')
        st.write('Rata - rata hasil pengukuran pH',rerata,'dinyatakan tidak memenuhi syarat keberterimaan')
        st.write('%RPD dari pengukuran pH',RPD,'tidak memenuhi syarat maka analisa dinyatakan tidak baik')
        st.write('Kadar alkali bebas',alkali,'dinyatakan tidak memenuhi syarat keberterimaan')
        st.write('Maka dapat disimpulkan bahwa Sabun Mandi Cair layak digunakan.')