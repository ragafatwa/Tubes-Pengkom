import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib
import datetime
from csv import writer

def save_data(arr, diskon, tot):
    with open('retails.csv', 'a', newline='') as f:
        write = writer(f)
        date = datetime.datetime.now()
        write.writerow([date , arr, diskon, tot])

def per_hour(date, df):

    df = df.loc[date]
    
    print(df)
    max = df['revenue'].max()
    min = df['revenue'].min()

    print("Penjualan hari ini terbesar adalah Rp{:,.1f}".format(max))
    print("Penjualan harian terkecil adalah Rp{:,.1f}".format(min))

    df_sum = df.resample('1H').sum()
    df_count = df.resample('1H').count()

    plt.suptitle(f"Summary of {date}")
    # Tabel ke 1
    plt.subplot(1,2,1)
    df_sum['revenue'].plot(x='date', y='revenue',kind='bar')

    plt.title('Total Pendapatan')
    plt.xlabel("jam")
    plt.xticks(rotation= 90)
    plt.xticks(range(0,24))
    plt.ylabel("Total Pendapatan")

    # Tabel ke 2
    plt.subplot(1,2,2)
    df_count['revenue'].plot(x='date', y='revenue', kind='bar')

    plt.title('Total Pengunjung')
    plt.xticks(rotation= 90)
    plt.xticks(range(0,24))
    plt.xlabel("jam")
    plt.ylabel("Jumlah Pelanggan")
    print(df_count)
    plt.show()

def per_day(month2, df):
    df = df.loc[df['month'] == month2]
    print(df)

    max = df['revenue'].max()
    min = df['revenue'].min()

    print("Penjualan Bulan ini terbesar adalah Rp{:,.1f}".format(max))
    print("Penjualan Bulan ini terkecil adalah Rp{:,.1f}".format(min))

    df_sum = df.resample('1D').sum()
    df_count = df.resample('1D').count()

    plt.suptitle(f"Summary of {month2}")
    # Tabel ke 1
    plt.subplot(1,2,1)
    df_sum['revenue'].plot(x='date', y='revenue',kind='bar')

    plt.title('Total Pendapatan')
    plt.xlabel("tanggal")
    plt.xticks(rotation= 90)
    plt.xticks(range(0,31))
    plt.ylabel("Total Pendapatan")

    # Tabel ke 2
    plt.subplot(1,2,2)
    df_count['revenue'].plot(x='date', y='revenue', kind='bar')

    plt.title('Total Pengunjung')
    plt.xticks(rotation= 90)
    plt.xticks(range(0,31))
    plt.xlabel("tanggal")
    plt.ylabel("Jumlah Pelanggan")
    print(df_count)
    plt.show()
    

def per_month(year, df):
    df = df.loc[df['year'] == str(year)]
    print(df)

    max = df['revenue'].max()
    min = df['revenue'].min()

    print("Penjualan Tahun ini terbesar adalah Rp{:,.1f}".format(max))
    print("Penjualan Tahun ini terkecil adalah Rp{:,.1f}".format(min))

    df_sum = df.resample('1M').sum()
    df_count = df.resample('1M').count()

    plt.suptitle(f"Summary of {year}")

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jly', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Tabel ke 1
    plt.subplot(1,2,1)
    df_sum['revenue'].plot(x='date', y='revenue',kind='bar')

    plt.title('Total Pendapatan')
    plt.xlabel("Bulan")
    plt.xticks(rotation= 80)
    plt.ylabel("Total Pendapatan")

    # Tabel ke 2
    plt.subplot(1,2,2)
    df_count['revenue'].plot(x='date', y='revenue', kind='bar')

    plt.title('Total Pengunjung')
    plt.xticks(rotation= 80)

    plt.xlabel("Bulan")
    plt.ylabel("Jumlah Pelanggan")
    # axes.set_xticks(range(0,12))
    # axes.set_xticklabels(months)
    print(df_count)
    plt.show()

def main():
    df = pd.read_csv('retails.csv')

    # Group by date
    temp = df
    print(df)
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')
    df['year'] = df['date'].dt.to_period('Y')
    df = df.set_index(['date'])
    df = df.sort_index()
    # print(df.describe())
    # print(df)

    print("Tampilan Opsi:\n1. Summary Penjualan Harian\n2. Summary Penjualan Bulanan\n3. Summary Penjualan Tahunan")
    pilihan = int(input("> "))

    if pilihan == 1:
        tanggal = (input("Silahkan Masukkan Tanggal (YYYY-MM-DD): "))
        per_hour(tanggal, df)
    elif pilihan == 2:
        bulan = (input("Silahkan Masukkan Bulan (YYYY-MM): "))
        per_day(bulan, df)
    elif pilihan == 3:
        tahun = int(input("Silahkan Masukkan Tahun (angka): "))
        per_month(tahun, df)

main()