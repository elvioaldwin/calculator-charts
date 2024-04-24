import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight", "Makan lebih banyak dan bergizi.", "#3498db"
    elif 18.5 <= bmi < 25:
        return "Normal", "Pertahankan pola makan dan olahraga yang baik.", "#2ecc71"
    elif 25 <= bmi < 30:
        return "Overweight", "Coba kurangi kalori dan tingkatkan aktivitas fisik.", "#f39c12"
    else:
        return "Obese", "Sangat disarankan untuk berkonsultasi dengan dokter atau ahli nutrisi.", "#e74c3c"

def display_bmi_info(bmi):
    category, advice, color = interpret_bmi(bmi)
    st.success(f'BMI Anda adalah {bmi:.2f}.')
    st.metric(label="Kategori", value=category, delta_color="off", help=advice)
    st.caption(advice)
    display_bmi_chart(bmi, category, color)

def display_bmi_chart(bmi, category, color):
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    values = [18.5, 24.9, 29.9, 40]
    user_bmi = [0, 0, 0, 0]
    index = categories.index(category)
    user_bmi[index] = bmi

    chart_data = {
        "Category": categories,
        "Max BMI": values,
        "User BMI": user_bmi
    }

    df = st.dataframe(chart_data)  # Optionally show the dataframe
    st.bar_chart(chart_data)

def main():
    st.title('Interactive BMI Calculator')
    st.write("### Anggota Kelompok:")
    st.write("""
    1. Elvio
    2. Prameshti
    3. Indana Zulfa
    4. Raden
    5. Nayla Rahma
    """)

    st.write("""
    ## Tentang Aplikasi Ini
    Aplikasi ini dibuat untuk memudahkan pengguna dalam menghitung dan memahami nilai BMI (Body Mass Index) mereka. 
    Dengan memasukkan berat dan tinggi badan, aplikasi ini akan menghitung BMI dan memberikan informasi tentang kategori 
    kesehatan yang sesuai dengan BMI tersebut.
    """)

    with st.sidebar:
        name = st.text_input("Masukkan nama Anda:")
        weight = st.number_input("Masukkan berat Anda (dalam kg):", min_value=1.0, format="%.2f")
        height = st.number_input("Masukkan tinggi Anda (dalam cm):", min_value=1.0, format="%.2f")
    
    if st.sidebar.button('Hitung BMI'):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            display_bmi_info(bmi)
        else:
            st.error("Mohon masukkan data yang valid!")

if __name__ == '__main__':
    main()
