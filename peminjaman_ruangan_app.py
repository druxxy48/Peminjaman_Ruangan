import tkinter as tk
import tkinter.messagebox as messagebox
from datetime import datetime
from tkinter import ttk
from tkcalendar import DateEntry
from database import Database


class PeminjamanRuanganApp:
    ############################################################### USER ###############################################################

    ############################################################### LOGIN PAGE ###############################################################
    def __init__(self, root):  # Inisialisasi atribut
        self.root = root
        self.root.title("Aplikasi Peminjaman Ruangan FEB")
        self.root.state("zoomed")

        # Database configuration
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "peminjaman_ruangan"
        }

        # Create database instance
        self.db = Database(**db_config)

        # Create main frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack()

        # Create header
        header_style = ttk.Style()
        header_style.configure(
            "Header.TLabel", font=("Inter", 20))

        label_header_user = ttk.Label(
            self.main_frame, text="Aplikasi Peminjaman Ruangan FEB", style="Header.TLabel"
        )
        label_header_user.pack(
            fill="x", expand=True, side="top", anchor="center", ipady=50)

        # Create labels
        judul_style = ttk.Style()
        judul_style.configure(
            "Judul.TLabel", font=("Inter", 16))
        label_judul_choose_user = ttk.Label(
            self.main_frame, text="Silahkan pilih user!", style="Judul.TLabel")
        label_judul_choose_user.pack(ipady=20, pady=(50, 0))

        # Create buttons
        button_style = ttk.Style()
        button_style.configure(
            "Button.TButton", font=("Inter", 16))
        mahasiswa_button = ttk.Button(
            self.main_frame, text="Login sebagai Mahasiswa", style="Button.TButton", command=self.on_mahasiswa_click)
        mahasiswa_button.pack(pady=15, ipadx=10, ipady=10)

        administrator_button = ttk.Button(
            self.main_frame, text="Login sebagai Administrator", style="Button.TButton", command=self.on_administrator_click)
        administrator_button.pack(pady=15, ipadx=10, ipady=10)

        # Create landing page frame
        self.create_landing_page()
        self.create_landing_page_admin()

        # Create cek room page frame
        self.create_cek_room_page()

        # Create status booking page frame
        self.create_status_booking_page()
        self.create_status_booking_page_admin()
        self.create_konfirmasi_booking_page_admin()
        self.create_form_konfirmasi_admin_page()

        # Create dokumentasi pengganti page frame
        self.create_dokumentasi_pengganti_page()

        # Create buat dokumentasi pengantian page frame
        self.create_form_dokumen_page()

        # Create buat booking page frame
        self.create_form_booking_page()

        # Initialize dropdown values
        self.update_dropdown_values_check_room()
        self.update_dropdown_values_buat_booking()
        self.update_dropdown_values_status_booking()
        self.update_dropdown_values_dokumentasi_pengganti()
        self.update_dropdown_values_status_booking_admin()
        self.update_dropdown_values_konfirmasi_booking_admin()

    def on_mahasiswa_click(self):
        self.main_frame.pack_forget()  # Sembunyikan halaman pemilihan jenis user
        self.landing_page_frame.pack()  # Tampilkan halaman landing page

############################################################### LANDING PAGE ###############################################################
    def create_landing_page(self):
        # Create frame for landing page
        self.landing_page_frame = tk.Frame(self.root, padx=20, pady=10)

        # Create header
        header_style = ttk.Style()
        header_style.configure(
            "Header.TLabel", font=("Inter", 20))

        label_header_user = ttk.Label(
            self.landing_page_frame, text="Aplikasi Peminjaman Ruangan FEB", style="Header.TLabel"
        )
        label_header_user.pack(
            fill="x", expand=True, side="top", anchor="center", ipady=40)

        # Create labels on landing page
        judul_style = ttk.Style()
        judul_style.configure(
            "Judul.TLabel", font=("Inter", 16))
        label_judul_landing_page = ttk.Label(
            self.landing_page_frame, text="Silahkan pilih opsi di bawah!", style="Judul.TLabel")
        label_judul_landing_page.pack(ipady=20, pady=(50, 0))

        # Create buttons on landing page
        button_style = ttk.Style()
        button_style.configure(
            "Button.TButton", font=("Inter", 16))
        cek_button = ttk.Button(
            self.landing_page_frame, text="Cek jadwal & Booking Ruangan", style="Button.TButton", command=self.on_cek_jadwal_booking_click)
        cek_button.pack(pady=15, ipadx=10, ipady=10)

        status_button = ttk.Button(
            self.landing_page_frame, text="Lihat Status Booking", style="Button.TButton", command=self.on_lihat_status_booking_click)
        status_button.pack(pady=15, ipadx=10, ipady=10)

        back_button = ttk.Button(self.landing_page_frame,
                                 text="Back", style="Button.TButton", command=self.on_back_click)
        back_button.pack(pady=15, ipadx=10, ipady=10)

    def on_cek_jadwal_booking_click(self):
        self.landing_page_frame.pack_forget()  # Sembunyikan halaman landing page
        self.cek_room_page_frame.pack()  # Tampilkan halaman cek room page

    def on_lihat_status_booking_click(self):
        self.landing_page_frame.pack_forget()
        self.status_booking_page_frame.pack()

    def on_back_click(self):
        self.landing_page_frame.pack_forget()  # Sembunyikan halaman landing page
        self.main_frame.pack()  # Tampilkan kembali halaman pemilihan jenis user

############################################################### CHECK ROOM PAGE ###############################################################
    def create_cek_room_page(self):
        # Create frame for cek room page
        self.cek_room_page_frame = tk.Frame(self.root, padx=20, pady=10)

        # Create header
        header_style = ttk.Style()
        header_style.configure(
            "Header.TLabel", font=("Inter", 20))

        label_header_user = ttk.Label(
            self.cek_room_page_frame, text="Aplikasi Peminjaman Ruangan FEB", style="Header.TLabel"
        )
        label_header_user.grid(row=1, column=0, columnspan=2, pady=40)

        # Create labels on cek room page
        judul_style = ttk.Style()
        judul_style.configure(
            "Judul.TLabel", font=("Inter", 16))
        label_judul = ttk.Label(self.cek_room_page_frame,
                                text="Jadwal Penggunaan Ruangan", style="Judul.TLabel")
        label_judul.grid(row=2, column=0, columnspan=2, pady=(50, 0))

        subjudul_style = ttk.Style()
        subjudul_style.configure(
            "Subjudul.TLabel", font=("Inter", 16))
        label_pilih_ruangan = ttk.Label(
            self.cek_room_page_frame, text="Silahkan pilih ruangan!", style="Subjudul.TLabel")
        label_pilih_ruangan.grid(row=3, column=0, columnspan=2, pady=(20, 30))

        # Create dropdown for room selection
        self.ruangan_var_check_room = tk.StringVar()
        self.ruangan_dropdown_check_room = ttk.Combobox(
            self.cek_room_page_frame, textvariable=self.ruangan_var_check_room, state='readonly')
        self.ruangan_dropdown_check_room.grid(
            row=4, column=0, pady=(20, 0), ipady=5, padx=(0, 10))

        # Create button to check schedule
        check_button_style = ttk.Style()
        check_button_style.configure(
            "Checkbutton.TButton", font=("Inter", 14))
        cek_jadwal_button = ttk.Button(
            self.cek_room_page_frame, text="Cek Jadwal", style="Checkbutton.TButton", command=self.on_cek_jadwal_button_click)
        cek_jadwal_button.grid(row=4, column=1, padx=10, pady=(20, 0))

        # Create subframe for additional buttons
        button_subframe = tk.Frame(self.cek_room_page_frame, padx=20, pady=10)
        button_subframe.grid(row=5, column=0, columnspan=2, pady=(20, 0))

        # Create back button
        button_style = ttk.Style()
        button_style.configure(
            "Button.TButton", font=("Inter", 16))
        back_button = ttk.Button(self.cek_room_page_frame, text="Back", style="Button.TButton",
                                 command=self.on_back_from_cek_room_page_click)
        back_button.grid(row=6, column=0, pady=(20, 0))

        # Create button to create new booking
        buat_booking_baru_button = ttk.Button(
            self.cek_room_page_frame, text="Buat Booking Baru", style="Button.TButton", command=self.on_buat_booking_baru_button_click)
        buat_booking_baru_button.grid(row=6, column=1, pady=(20, 0), padx=10)

        # Hide cek room page initially
        self.cek_room_page_frame.pack_forget()

    def update_dropdown_values_check_room(self):
        # Ambil ruangan dari database dan perbarui nilai dropdown
        query = "SELECT room_name FROM room"
        rooms = self.db.fetch_data(query)
        self.ruangan_dropdown_check_room['values'] = [
            room[0] for room in rooms]

    def on_cek_jadwal_button_click(self):
        selected_ruangan = self.ruangan_var_check_room.get()

        # Query untuk mendapatkan data jadwal peminjaman dengan pengurutan berdasarkan waktu mulai
        query = """
            SELECT
                room.room_name AS NamaRuangan,
                CONCAT(reservation.booker_name, ' - ', reservation.booker_npm, ' - ', reservation.booker_major) AS IdentitasPeminjam,
                reservation.checkin_date AS WaktuMulaiPeminjaman,
                reservation.checkout_date AS WaktuSelesaiPeminjaman
            FROM
                reservation
            JOIN room ON reservation.room_id = room.id
            WHERE
                room.room_name = %s
            ORDER BY
                reservation.checkin_date
        """

        # Eksekusi query dengan parameter ruangan yang dipilih
        data = (selected_ruangan,)
        result = self.db.fetch_data(query, data)

        # Tampilkan hasil query dalam bentuk tabel
        self.display_table_cek_room(result)

        # Create back button
        back_button = ttk.Button(self.cek_room_page_frame, text="Back", style="Button.TButton",
                                 command=self.on_back_from_cek_room_page_click)
        back_button.grid(row=6, column=0, padx=10, pady=(20, 0))

        # Create button to create new booking
        buat_booking_baru_button = ttk.Button(
            self.cek_room_page_frame, text="Buat Booking Baru", style="Button.TButton", command=self.on_buat_booking_baru_button_click)
        buat_booking_baru_button.grid(row=6, column=1, padx=10, pady=(20, 0))

    def display_table_cek_room(self, data):
        # Hapus widget tabel sebelumnya (jika ada)
        for widget in self.cek_room_page_frame.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.pack_forget()

        # Create table frame
        table_frame = tk.Frame(self.cek_room_page_frame)
        table_frame.grid(row=5, column=0, columnspan=2, pady=(40, 20))

        # Create Treeview (table) with vertical scrollbar
        columns = ("No", "Nama Ruangan", "Identitas Peminjam",
                   "Waktu Mulai Peminjaman", "Waktu Selesai Peminjaman")
        self.table_cek_room = ttk.Treeview(
            table_frame, columns=columns, show="headings", height=5)

        # Configure column widths
        column_widths = [50, 150, 200, 150, 150]
        for col, width in zip(columns, column_widths):
            self.table_cek_room.column(col, width=width, anchor="center")

        # Configure column headings
        for col in columns:
            self.table_cek_room.heading(col, text=col)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.table_cek_room.yview)
        self.table_cek_room.configure(yscrollcommand=scrollbar.set)

        # Pack components
        self.table_cek_room.pack(side="left")
        scrollbar.pack(side="right", fill="y")

        # Add data to the table
        for i, row in enumerate(data, start=1):
            self.table_cek_room.insert("", "end", values=(i,) + row)

    def on_buat_booking_baru_button_click(self):
        self.cek_room_page_frame.pack_forget()  # Sembunyikan halaman cek room page
        self.form_booking_page_frame.pack()  # Tampilkan halaman buat booking page

    def on_back_from_cek_room_page_click(self):
        self.cek_room_page_frame.pack_forget()  # Sembunyikan halaman cek room page
        self.landing_page_frame.pack()  # Tampilkan kembali halaman landing page

############################################################### STATUS BOOKING PAGE ###############################################################
    def create_status_booking_page(self):
        # Create frame for status booking
        self.status_booking_page_frame = tk.Frame(self.root, padx=20, pady=10)

        # Create header
        header_style = ttk.Style()
        header_style.configure(
            "Header.TLabel", font=("Inter", 20))

        label_header_user = ttk.Label(
            self.status_booking_page_frame, text="Aplikasi Peminjaman Ruangan FEB", style="Header.TLabel"
        )
        label_header_user.grid(row=1, column=0, columnspan=2, pady=40)

        # Create labels on status booking
        judul_style = ttk.Style()
        judul_style.configure(
            "Judul.TLabel", font=("Inter", 20))
        label_judul = ttk.Label(
            self.status_booking_page_frame, text="Status Booking Ruangan", style="Judul.TLabel")
        label_judul.grid(row=2, column=0, columnspan=2, pady=(50, 0))

        subjudul_style = ttk.Style()
        subjudul_style.configure(
            "Subjudul.TLabel", font=("Inter", 14))
        label_pilih_ruangan = ttk.Label(
            self.status_booking_page_frame, text="Silahkan pilih ruangan!", style="Subjudul.TLabel")
        label_pilih_ruangan.grid(row=3, column=0, columnspan=2, pady=(20, 0))

        # Create dropdown for room selection
        self.ruangan_var_status_booking = tk.StringVar()
        self.ruangan_dropdown_status_booking = ttk.Combobox(
            self.status_booking_page_frame, textvariable=self.ruangan_var_status_booking, state='readonly')
        self.ruangan_dropdown_status_booking.grid(
            row=4, column=0, pady=(20, 0), ipady=5, padx=(0, 10))

        # Create button to status booking
        check_button_style = ttk.Style()
        check_button_style.configure(
            "Checkbutton.TButton", font=("Inter", 14))
        cek_status_booking = ttk.Button(
            self.status_booking_page_frame, text="Cek Status", style="Checkbutton.TButton", command=self.on_cek_status_booking_click)
        cek_status_booking.grid(row=4, column=1, padx=10, pady=(20, 0))

        # Create subframe for additional buttons
        button_subframe = tk.Frame(
            self.status_booking_page_frame, padx=20, pady=15)
        button_subframe.grid(row=5, column=0, columnspan=2, pady=15)

        # Create back button
        button_style = ttk.Style()
        button_style.configure(
            "Button.TButton", font=("Inter", 16))
        back_button = ttk.Button(self.status_booking_page_frame, text="Back", style="Checkbutton.TButton",
                                 command=self.on_back_from_status_booking_page_click)
        back_button.grid(row=6, column=0, pady=(20, 0))

        # Create button to create new booking
        dokumentasi_pengganti_button = ttk.Button(
            self.status_booking_page_frame, text="Buat Dokumen Penggantian Kerusakan", style="Checkbutton.TButton", command=self.on_dokumentasi_pengganti_button_click)
        dokumentasi_pengganti_button.grid(row=6, column=1, pady=(20, 0))

        # Hide cek room page initially
        self.status_booking_page_frame.pack_forget()

    def update_dropdown_values_status_booking(self):
        # Ambil ruangan dari database dan perbarui nilai dropdown
        query = "SELECT room_name FROM room"
        rooms = self.db.fetch_data(query)
        self.ruangan_dropdown_status_booking['values'] = [
            room[0] for room in rooms]

    def on_cek_status_booking_click(self):
        selected_ruangan = self.ruangan_var_status_booking.get()

        # Query untuk mendapatkan data jadwal peminjaman dengan pengurutan berdasarkan waktu mulai
        query = """
            SELECT
                room.room_name AS NamaRuangan,
                CONCAT(reservation.booker_name, ' - ', reservation.booker_npm, ' - ', reservation.booker_major) AS IdentitasPeminjam,
                CONCAT(reservation.checkin_date, ' -> ', reservation.checkout_date) AS WaktuPeminjaman,
                reservation.approval_status AS StatusBooking,
                reservation.facility_check_status AS StatusFacility
            FROM
                reservation
            JOIN room ON reservation.room_id = room.id
            WHERE
                room.room_name = %s
            ORDER BY
                reservation.checkin_date
        """

        # Eksekusi query dengan parameter ruangan yang dipilih
        data = (selected_ruangan,)
        result = self.db.fetch_data(query, data)

        # Tampilkan hasil query dalam bentuk tabel
        self.display_table_status_booking(result)

        # Create back button
        back_button = ttk.Button(self.status_booking_page_frame, text="Back", style="Checkbutton.TButton",
                                 command=self.on_back_from_status_booking_page_click)
        back_button.grid(row=6, column=0, padx=10, pady=(20, 0))

        # Create button to create new booking
        dokumentasi_pengganti_button = ttk.Button(
            self.status_booking_page_frame, text="Buat Dokumen Penggantian Kerusakan", style="Checkbutton.TButton", command=self.on_dokumentasi_pengganti_button_click)
        dokumentasi_pengganti_button.grid(
            row=6, column=1, padx=10, pady=(20, 0))

    def display_table_status_booking(self, data):
        # Hapus widget tabel sebelumnya (jika ada)
        for widget in self.status_booking_page_frame.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.pack_forget()

        # Create table frame
        table_frame = tk.Frame(self.status_booking_page_frame)
        table_frame.grid(row=5, column=0, columnspan=2, pady=20)

        # Create Treeview (table) with vertical scrollbar
        columns = ("No", "Nama Ruangan", "Identitas Peminjam",
                   "Waktu Peminjaman", "Status Booking", "Status Fasilitas")
        self.table_buat_booking = ttk.Treeview(
            table_frame, columns=columns, show="headings", height=5)

        # Configure column widths
        column_widths = [50, 125, 225, 200, 200, 200]
        for col, width in zip(columns, column_widths):
            self.table_buat_booking.column(col, width=width, anchor="center")

        # Configure column headings
        for col in columns:
            self.table_buat_booking.heading(col, text=col)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.table_buat_booking.yview)
        self.table_buat_booking.configure(yscrollcommand=scrollbar.set)

        # Pack components
        self.table_buat_booking.pack(side="left")
        scrollbar.pack(side="right", fill="y")

        # Add data to the table
        for i, row in enumerate(data, start=1):
            # Replace None or NULL with '-'
            modified_row = tuple(
                [(col if col is not None else '-') for col in row])
            self.table_buat_booking.insert(
                "", "end", values=(i,) + modified_row)

    def on_dokumentasi_pengganti_button_click(self):
        self.status_booking_page_frame.pack_forget()  # Sembunyikan halaman cek room page
        # Tampilkan halaman buat booking page
        self.dokumentasi_pengganti_page_frame.pack()

    def on_back_from_status_booking_page_click(self):
        self.status_booking_page_frame.pack_forget()  # Sembunyikan halaman cek room page
        self.landing_page_frame.pack()  # Tampilkan kembali halaman landing page

############################################################### FORM BOOKING PAGE ###############################################################
    def create_form_booking_page(self):
        self.form_booking_page_frame = tk.Frame(root, padx=20, pady=10)

        # Create header
        header_style = ttk.Style()
        header_style.configure(
            "Header.TLabel", font=("Inter", 20))

        label_header_user = ttk.Label(
            self.form_booking_page_frame, text="Aplikasi Peminjaman Ruangan FEB", style="Header.TLabel"
        )
        label_header_user.grid(row=1, column=0, columnspan=2, pady=40)

        # Create labels
        judul_style = ttk.Style()
        judul_style.configure(
            "Judul.TLabel", font=("Inter", 16))
        label_judul = ttk.Label(
            self.form_booking_page_frame, text="Booking Ruangan", style="Judul.TLabel")
        label_judul.grid(row=2, column=0, columnspan=2, pady=10)

        subjudul_style = ttk.Style()
        subjudul_style.configure(
            "Subjudul.TLabel", font=("Inter", 14))
        label_instruksi = ttk.Label(
            self.form_booking_page_frame, text="Silahkan isi formulir di bawah ini!", style="Subjudul.TLabel")
        label_instruksi.grid(row=3, column=0, columnspan=2, pady=10)

        form_label_style = ttk.Style()
        form_label_style.configure(
            "FormLabel.TLabel", font=("Inter", 12))
        label_ruangan = ttk.Label(
            self.form_booking_page_frame, text="Ruangan", style="FormLabel.TLabel")
        label_ruangan.grid(row=4, column=0, pady=20)

        # Create dropdown for room selection
        self.ruangan_var_form = tk.StringVar()
        self.ruangan_dropdown_form = ttk.Combobox(
            self.form_booking_page_frame, textvariable=self.ruangan_var_form, state='readonly')
        self.ruangan_dropdown_form.grid(row=4, column=1, pady=20)

        # Create form elements
        label_nama = ttk.Label(
            self.form_booking_page_frame, text="Nama Peminjam", style="FormLabel.TLabel")
        label_nama.grid(row=5, column=0, pady=20)

        self.entry_nama = ttk.Entry(self.form_booking_page_frame)
        self.entry_nama.grid(row=5, column=1, pady=20)

        label_npm = ttk.Label(
            self.form_booking_page_frame, text="NPM Peminjam", style="FormLabel.TLabel")
        label_npm.grid(row=6, column=0, pady=20)

        self.entry_npm = ttk.Entry(self.form_booking_page_frame)
        self.entry_npm.grid(row=6, column=1, pady=20)

        label_email = ttk.Label(
            self.form_booking_page_frame, text="Email Peminjam", style="FormLabel.TLabel")
        label_email.grid(row=7, column=0, pady=20)

        self.entry_email = ttk.Entry(self.form_booking_page_frame)
        self.entry_email.grid(row=7, column=1, pady=20)

        label_prodi = ttk.Label(
            self.form_booking_page_frame, text="Prodi Peminjam", style="FormLabel.TLabel")
        label_prodi.grid(row=8, column=0, pady=20)

        self.entry_prodi = ttk.Entry(self.form_booking_page_frame)
        self.entry_prodi.grid(row=8, column=1, pady=20)

        label_no_hp = ttk.Label(
            self.form_booking_page_frame, text="No HP Peminjam", style="FormLabel.TLabel")
        label_no_hp.grid(row=9, column=0, pady=20)

        self.entry_no_hp = ttk.Entry(self.form_booking_page_frame)
        self.entry_no_hp.grid(row=9, column=1, pady=20)

        label_mulai = ttk.Label(
            self.form_booking_page_frame, text="Waktu Mulai Peminjaman", style="FormLabel.TLabel")
        label_mulai.grid(row=10, column=0, pady=20)

        # Create calendar entry for start time
        self.mulai_cal = DateEntry(self.form_booking_page_frame, width=15,
                                   background='darkblue', foreground='white', borderwidth=2, values=datetime.now())
        self.mulai_cal.grid(row=10, column=1, pady=20)

        label_selesai = ttk.Label(
            self.form_booking_page_frame, text="Waktu Selesai Peminjaman", style="FormLabel.TLabel")
        label_selesai.grid(row=11, column=0, pady=20)

        # Create calendar entry for end time
        self.selesai_cal = DateEntry(self.form_booking_page_frame, width=15,
                                     background='darkblue', foreground='white', borderwidth=2, values=datetime.now())
        self.selesai_cal.grid(row=11, column=1, pady=20)

        # Create buttons
        button_style = ttk.Style()
        button_style.configure(
            "Button.TButton", font=("Inter", 16))
        back_button = ttk.Button(self.form_booking_page_frame, text="Back", style="Button.TButton",
                                 command=self.on_back_from_form_booking_page_click)
        back_button.grid(row=12, column=0, pady=15)

        buat_booking_button = ttk.Button(
            self.form_booking_page_frame, text="Buat Booking", style="Button.TButton", command=self.on_buat_booking_button_click)
        buat_booking_button.grid(row=12, column=1, pady=15)

        # Hide buat booking page initially
        self.form_booking_page_frame.pack_forget()

    def update_dropdown_values_buat_booking(self):
        # Ambil ruangan dari database dan perbarui nilai dropdown
        query = "SELECT room_name FROM room"
        rooms = self.db.fetch_data(query)
        self.ruangan_dropdown_form['values'] = [room[0] for room in rooms]

    def on_buat_booking_button_click(self):
        # Get values from the form
        selected_ruangan = self.ruangan_var_form.get()
        booker_name = self.entry_nama.get()
        booker_npm = self.entry_npm.get()
        booker_email = self.entry_email.get()
        booker_major = self.entry_prodi.get()
        booker_phone = self.entry_no_hp.get()
        checkin_date = self.mulai_cal.get_date().strftime('%Y-%m-%d')
        checkout_date = self.selesai_cal.get_date().strftime('%Y-%m-%d')

        # Fetch room_id based on the selected room name
        query_room_id = "SELECT id FROM room WHERE room_name = %s"
        room_id_data = (selected_ruangan,)
        room_id_result = self.db.fetch_data(query_room_id, room_id_data)

        if room_id_result:
            room_id = room_id_result[0][0]

            # Insert booking data into the reservation table
            query_insert_booking = """
                INSERT INTO reservation (room_id, booker_name, booker_npm, booker_email, booker_major, booker_phone_number, checkin_date, checkout_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            booking_data = (room_id, booker_name, booker_npm, booker_email,
                            booker_major, booker_phone, checkin_date, checkout_date)
            self.db.execute_query(query_insert_booking, booking_data)

            messagebox.showinfo("Success", "Booking berhasil dibuat!")

            # Clear entry fields
            self.ruangan_var_form.set('')
            self.entry_nama.delete(0, tk.END)
            self.entry_npm.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.entry_prodi.delete(0, tk.END)
            self.entry_no_hp.delete(0, tk.END)
            self.mulai_cal.set_date(datetime.now())
            self.selesai_cal.set_date(datetime.now())
        else:
            messagebox.showerror("Error", "Gagal mendapatkan ID ruangan.")

    def on_back_from_form_booking_page_click(self):
        # Sembunyikan halaman buat booking page
        self.form_booking_page_frame.pack_forget()
        self.cek_room_page_frame.pack()  # Tampilkan kembali halaman cek room page

############################################################### DOKUMENTASI PENGGANTI PAGE ###############################################################
    def create_dokumentasi_pengganti_page(self):
        # Create frame for cek room page
        self.dokumentasi_pengganti_page_frame = tk.Frame(
            self.root, padx=20, pady=10)

        # Create header
        header_style = ttk.Style()
        header_style.configure(
            "Header.TLabel", font=("Inter", 20))

        label_header_user = ttk.Label(
            self.dokumentasi_pengganti_page_frame, text="Aplikasi Peminjaman Ruangan FEB", style="Header.TLabel"
        )
        label_header_user.grid(row=1, column=0, columnspan=2, pady=40)

        # Create labels
        judul_style = ttk.Style()
        judul_style.configure(
            "Judul.TLabel", font=("Inter", 16))
        label_judul = ttk.Label(
            self.dokumentasi_pengganti_page_frame, text="Penggantian Kerusakan Fasilitas", style="Judul.TLabel")
        label_judul.grid(row=2, column=0, columnspan=2, pady=10)

        subjudul_style = ttk.Style()
        subjudul_style.configure(
            "Subjudul.TLabel", font=("Inter", 16))
        label_pilih_ruangan = ttk.Label(
            self.dokumentasi_pengganti_page_frame, text="Silahkan pilih ruangan!", style="Subjudul.TLabel")
        label_pilih_ruangan.grid(row=3, column=0, columnspan=2, pady=10)

        # Create dropdown for room selection
        self.ruangan_var_dokumentasi_pengganti = tk.StringVar()
        self.ruangan_dropdown_dokumentasi_pengganti = ttk.Combobox(
            self.dokumentasi_pengganti_page_frame, textvariable=self.ruangan_var_dokumentasi_pengganti, state='readonly')
        self.ruangan_dropdown_dokumentasi_pengganti.grid(
            row=4, column=0, pady=15)

        # Create button to status booking
        check_button_style = ttk.Style()
        check_button_style.configure(
            "Checkbutton.TButton", font=("Inter", 14))
        cek_status_dokumentasi_pengganti = ttk.Button(
            self.dokumentasi_pengganti_page_frame, text="Cek Status", style="Checkbutton.TButton", command=self.on_cek_status_dokumentasi_pengganti_click)
        cek_status_dokumentasi_pengganti.grid(
            row=4, column=1, pady=15, padx=(10, 0))

        # Create back button
        button_style = ttk.Style()
        button_style.configure(
            "Button.TButton", font=("Inter", 16))
        back_button = ttk.Button(self.dokumentasi_pengganti_page_frame,
                                 text="Back", style="Button.TButton", command=self.on_back_from_dokumentasi_pengganti_click)
        back_button.grid(row=6, column=0, pady=10)

        # Hide cek room page initially
        self.dokumentasi_pengganti_page_frame.pack_forget()

    def update_dropdown_values_dokumentasi_pengganti(self):
        # Ambil ruangan dari database dan perbarui nilai dropdown
        query = "SELECT room_name FROM room"
        rooms = self.db.fetch_data(query)
        self.ruangan_dropdown_dokumentasi_pengganti['values'] = [
            room[0] for room in rooms]

    def on_cek_status_dokumentasi_pengganti_click(self):
        selected_ruangan = self.ruangan_var_dokumentasi_pengganti.get()

        # Query untuk mendapatkan data jadwal peminjaman dengan pengurutan berdasarkan waktu mulai
        query = """
            SELECT
                reservation.id As ReservationId,
                room.room_name AS NamaRuangan,
                CONCAT(reservation.booker_name, ' - ', reservation.booker_npm, ' - ', reservation.booker_major) AS IdentitasPeminjam,
                CONCAT(reservation.checkin_date, ' -> ', reservation.checkout_date) AS WaktuPeminjaman,
                facility_replacement.replacement_status AS Status
            FROM
                reservation
            JOIN room ON reservation.room_id = room.id
            JOIN facility_replacement ON reservation.id = facility_replacement.reservation_id
            WHERE
                room.room_name = %s
            ORDER BY
                reservation.checkin_date
        """

        # Eksekusi query dengan parameter ruangan yang dipilih
        data = (selected_ruangan,)
        result = self.db.fetch_data(query, data)

        # Tampilkan hasil query dalam bentuk tabel
        self.display_table_dokumentasi_pengganti(result)

        # Create back button
        back_button = ttk.Button(self.dokumentasi_pengganti_page_frame,
                                 text="Back", style="Button.TButton", command=self.on_back_from_dokumentasi_pengganti_click)
        back_button.grid(row=6, column=0, pady=10)

    def display_table_dokumentasi_pengganti(self, data):
        # Hapus widget tabel sebelumnya (jika ada)
        for widget in self.dokumentasi_pengganti_page_frame.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.pack_forget()

        # Create table frame
        table_frame = tk.Frame(self.dokumentasi_pengganti_page_frame)
        table_frame.grid(row=5, column=0, columnspan=3, pady=10)

        # Create Treeview (table) with vertical scrollbar
        columns = ("No", "Nama Ruangan", "Identitas Peminjam",
                   "Waktu Peminjaman", "Status")
        self.table_dokumentasi_pengganti = ttk.Treeview(
            table_frame, columns=columns, show="headings", height=5)

        # Configure column widths
        column_widths = [50, 150, 200, 150, 150]
        for col, width in zip(columns, column_widths):
            self.table_dokumentasi_pengganti.column(
                col, width=width, anchor="center")

        # Configure column headings
        for col in columns:
            self.table_dokumentasi_pengganti.heading(col, text=col)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.table_dokumentasi_pengganti.yview)
        self.table_dokumentasi_pengganti.configure(
            yscrollcommand=scrollbar.set)

        # Pack components
        self.table_dokumentasi_pengganti.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        for i, row in enumerate(data, start=1):
            # Replace None or NULL with '-'
            modified_row = tuple(
                [(col if col is not None else '-') for col in row])
            # Insert data into the table
            values = (i,) + modified_row[1:]
            item_id = self.table_dokumentasi_pengganti.insert(
                "", "end", values=values)

            # Jika status adalah "Buat Dokumen Penggantian Fasilitas", tambahkan fungsi klik untuk direct ke form penggantian page
            if modified_row[4] == "Buat Dokumen Penggantian Fasilitas":
                self.table_dokumentasi_pengganti.tag_configure(
                    f"action_button_{i}", background="lightblue")
                self.table_dokumentasi_pengganti.tag_bind(
                    f"action_button_{i}", "<Button-1>", lambda event, data=modified_row: self.on_buat_dokumen_pengganti_click(data))
                self.table_dokumentasi_pengganti.item(
                    item_id, tags=(f"action_button_{i}",))

    def on_buat_dokumen_pengganti_click(self, data):
        reservation_id = data[0]

        query = """
            SELECT
                reservation.id AS ReservationId,
                room.id AS RoomId,
                room.room_name AS NamaRuangan,
                reservation.booker_name AS NamaPeminjam, 
                reservation.booker_npm AS NpmPeminjam, 
                reservation.booker_email AS EmailPeminjam, 
                reservation.booker_major AS ProdiPeminjam,
                reservation.booker_phone_number AS NoHpPeminjam
            FROM
                reservation
            JOIN room ON reservation.room_id = room.id
            WHERE
                reservation.id = %s
        """
        data = (reservation_id,)
        result = self.db.fetch_data(query, data)

        # Unpack the result and assign values to the corresponding variables
        (reserv_id, room_id, ruangan, nama, npm,
         email, prodi, nomor_hp) = result[0]

        # Hide the current page
        self.dokumentasi_pengganti_page_frame.pack_forget()

        # Show the new form page
        self.form_dokumen_page_frame.pack()

        # Set values to the corresponding labels/entries in the form
        self.reservation_id_fp = reserv_id
        self.room_id_fp = room_id
        self.label_ruangan_fp.config(text=ruangan)
        self.entry_nama_fp.config(text=nama)
        self.entry_npm_fp.config(text=npm)
        self.entry_email_fp.config(text=email)
        self.entry_prodi_fp.config(text=prodi)
        self.entry_no_hp_fp.config(text=nomor_hp)

    def on_back_from_dokumentasi_pengganti_click(self):
        self.dokumentasi_pengganti_page_frame.pack_forget()
        self.status_booking_page_frame.pack()

############################################################### FORM DOKUMEN PAGE ###############################################################
    def create_form_dokumen_page(self):
        self.form_dokumen_page_frame = tk.Frame(root, padx=20, pady=10)

        # Create header
        header_style = ttk.Style()
        header_style.configure(
            "Header.TLabel", font=("Inter", 20))

        label_header_user = ttk.Label(
            self.form_dokumen_page_frame, text="Aplikasi Peminjaman Ruangan FEB", style="Header.TLabel"
        )
        label_header_user.grid(row=1, column=0, columnspan=2, pady=40)

        # Create labels
        judul_style = ttk.Style()
        judul_style.configure(
            "Judul.TLabel", font=("Inter", 16))
        label_judul = ttk.Label(
            self.form_dokumen_page_frame, text="Formulir Penggantian Kerusakan Fasilitas", style="Judul.TLabel")
        label_judul.grid(row=2, column=0, columnspan=2, pady=10)

        subjudul_style = ttk.Style()
        subjudul_style.configure(
            "Subjudul.TLabel", font=("Inter", 14))
        label_instruksi = ttk.Label(
            self.form_dokumen_page_frame, text="Silahkan isi Formulir di bawah ini!", style="Subudul.TLabel")
        label_instruksi.grid(row=3, column=0, columnspan=2, pady=10)

        # Create form elements
        form_label_style = ttk.Style()
        form_label_style.configure(
            "FormLabel.TLabel", font=("Inter", 12))
        label_ruangan = ttk.Label(
            self.form_dokumen_page_frame, text="Ruangan", style="FormLabel.TLabel")
        label_ruangan.grid(row=4, column=0, pady=20)

        self.label_ruangan_fp = ttk.Label(
            self.form_dokumen_page_frame, text="")
        self.label_ruangan_fp.grid(row=4, column=1, pady=20)

        label_nama = ttk.Label(
            self.form_dokumen_page_frame, text="Nama Peminjam", style="FormLabel.TLabel")
        label_nama.grid(row=5, column=0, pady=20)

        self.entry_nama_fp = ttk.Label(self.form_dokumen_page_frame, text="")
        self.entry_nama_fp.grid(row=5, column=1, pady=20)

        label_npm = ttk.Label(
            self.form_dokumen_page_frame, text="NPM Peminjam", style="FormLabel.TLabel")
        label_npm.grid(row=6, column=0, pady=20)

        self.entry_npm_fp = ttk.Label(self.form_dokumen_page_frame, text="")
        self.entry_npm_fp.grid(row=6, column=1, pady=20)

        label_email = ttk.Label(
            self.form_dokumen_page_frame, text="Email Peminjam", style="FormLabel.TLabel")
        label_email.grid(row=7, column=0, pady=20)

        self.entry_email_fp = ttk.Label(self.form_dokumen_page_frame, text="")
        self.entry_email_fp.grid(row=7, column=1, pady=20)

        label_prodi = ttk.Label(
            self.form_dokumen_page_frame, text="Prodi Peminjam", style="FormLabel.TLabel")
        label_prodi.grid(row=8, column=0, pady=20)

        self.entry_prodi_fp = ttk.Label(self.form_dokumen_page_frame, text="")
        self.entry_prodi_fp.grid(row=8, column=1, pady=20)

        label_no_hp = ttk.Label(
            self.form_dokumen_page_frame, text="No HP Peminjam", style="FormLabel.TLabel")
        label_no_hp.grid(row=9, column=0, pady=20)

        self.entry_no_hp_fp = ttk.Label(self.form_dokumen_page_frame, text="")
        self.entry_no_hp_fp.grid(row=9, column=1, pady=20)

        label_deskripsi = ttk.Label(
            self.form_dokumen_page_frame, text="Deskripsi Penggantian Kerusakan Fasilitas", style="FormLabel.TLabel")
        label_deskripsi.grid(row=10, column=0, pady=20)

        self.entry_deskripsi_fp = ttk.Entry(self.form_dokumen_page_frame)
        self.entry_deskripsi_fp.grid(row=10, column=1, pady=20)

        # Create buttons
        button_style = ttk.Style()
        button_style.configure(
            "Button.TButton", font=("Inter", 16))
        back_button = ttk.Button(self.form_dokumen_page_frame, text="Back",
                                 command=self.on_back_from_form_dokumen_page_click, style="Button.TButton")
        back_button.grid(row=11, column=0, pady=20)

        buat_dokumen_kerusakan_button = ttk.Button(
            self.form_dokumen_page_frame, text="Buat Dokumen", command=self.on_buat_dokumen_kerusakan_button_click, style="Button.TButton")
        buat_dokumen_kerusakan_button.grid(row=11, column=1, pady=20)

        # Hide buat booking page initially
        self.form_dokumen_page_frame.pack_forget()

    def on_buat_dokumen_kerusakan_button_click(self):
        # Get Ids
        reserv_id = self.reservation_id_fp
        room_id = self.room_id_fp
        # Get values from the form
        deskripsi = self.entry_deskripsi_fp.get()

        # Fetch facility_replacement_id based on room_id and reservation_id
        query_replacement_id = """
            SELECT id FROM facility_replacement
            WHERE room_id = %s AND reservation_id = %s
        """
        replacement_id_data = (room_id, reserv_id)
        replacement_id_result = self.db.fetch_data(
            query_replacement_id, replacement_id_data)

        # Check if deskripsi is empty
        if not deskripsi.strip():
            messagebox.showerror(
                "Error", "Deskripsi harus diisi untuk membuat dokumen kerusakan.")
            return
        else:
            replacement_id = replacement_id_result[0][0]

            # Update facility replacement data
            query_update_replacement = """
                UPDATE facility_replacement
                SET replacement_desc = %s, replacement_status = %s
                WHERE id = %s
            """
            replacement_data = (
                deskripsi, "Menunggu Verifikasi Dokumen", replacement_id)
            self.db.execute_query(query_update_replacement, replacement_data)

            # Update reservation status
            query_update_reservation_status = """
                UPDATE reservation
                SET facility_check_status = %s
                WHERE id = %s
            """
            reservation_facilitt_check_status_data = (
                "Menunggu Konfirmasi Pergantian Fasilitas", reserv_id)
            self.db.execute_query(
                query_update_reservation_status, reservation_facilitt_check_status_data)

            messagebox.showinfo("Success", "Dokumen berhasil dibuat!")

            # Clear entry fields
            self.entry_deskripsi_fp.delete(0, tk.END)

            # Refresh the table data
            query_room_name = "SELECT room_name FROM room WHERE id = %s"
            room_name_data = (room_id,)
            room_name = self.db.fetch_data(query_room_name, room_name_data)

            query_show_data = """
                SELECT
                    reservation.id As ReservationId,
                    room.room_name AS NamaRuangan,
                    CONCAT(reservation.booker_name, ' - ', reservation.booker_npm, ' - ', reservation.booker_major) AS IdentitasPeminjam,
                    CONCAT(reservation.checkin_date, ' -> ', reservation.checkout_date) AS WaktuPeminjaman,
                    facility_replacement.replacement_status AS Status
                FROM
                    reservation
                JOIN room ON reservation.room_id = room.id
                JOIN facility_replacement ON reservation.id = facility_replacement.reservation_id
                WHERE
                    room.room_name = %s
                ORDER BY
                    reservation.checkin_date
            """

            # Eksekusi query dengan parameter ruangan yang dipilih
            table_data = (room_name[0][0],)
            result = self.db.fetch_data(query_show_data, table_data)

            self.display_table_dokumentasi_pengganti(result)

            self.form_dokumen_page_frame.pack_forget()
            self.dokumentasi_pengganti_page_frame.pack()

    def on_back_from_form_dokumen_page_click(self):
        # Sembunyikan halaman buat booking page
        self.form_dokumen_page_frame.pack_forget()
        # Tampilkan kembali halaman cek room page
        self.dokumentasi_pengganti_page_frame.pack()

############################################################### ADMIN ###############################################################

############################################################### LOGIN PAGE ###############################################################
    def on_administrator_click(self):
        self.main_frame.pack_forget()  # Sembunyikan halaman pemilihan jenis user
        self.landing_page_admin_frame.pack()  # Tampilkan halaman landing page

############################################################### lANDING PAGE ###############################################################
    def create_landing_page_admin(self):
        # Create frame for landing page
        self.landing_page_admin_frame = tk.Frame(self.root, padx=20, pady=10)

        # Create header
        header_style = ttk.Style()
        header_style.configure(
            "Header.TLabel", font=("Inter", 20))

        label_header_user = ttk.Label(
            self.landing_page_admin_frame, text="Aplikasi Peminjaman Ruangan FEB", style="Header.TLabel"
        )
        label_header_user.pack(
            fill="x", expand=True, side="top", anchor="center", ipady=50)

        # Create labels
        judul_style = ttk.Style()
        judul_style.configure(
            "Judul.TLabel", font=("Inter", 16))
        label_judul_landing_page = ttk.Label(
            self.landing_page_admin_frame, text="Silahkan pilih opsi di bawah!", style="Judul.TLabel")
        label_judul_landing_page.pack(padx=20, pady=20)

        # Create buttons on landing page
        button_style = ttk.Style()
        button_style.configure(
            "Button.TButton", font=("Inter", 16))
        cek_button = ttk.Button(self.landing_page_admin_frame, text="Konfirmasi Booking Ruangan", style="Button.TButton",
                                command=self.on_konfirmasi_booking_admin_click)
        cek_button.pack(pady=20)

        status_button = ttk.Button(self.landing_page_admin_frame, text="Lihat Status Booking", style="Button.TButton",
                                   command=self.on_lihat_status_booking_admin_click)
        status_button.pack(pady=20)

        back_button = ttk.Button(
            self.landing_page_admin_frame, text="Back", style="Button.TButton", command=self.on_back_admin_click)
        back_button.pack(pady=20)

    def on_konfirmasi_booking_admin_click(self):
        self.landing_page_admin_frame.pack_forget()  # Tampilkan halaman cek room page
        # Sembunyikan halaman landing page
        self.konfirmasi_booking_page_admin_frame.pack()

    def on_lihat_status_booking_admin_click(self):
        self.landing_page_admin_frame.pack_forget()
        self.status_booking_page_admin_frame.pack()

    def on_back_admin_click(self):
        self.landing_page_admin_frame.pack_forget()  # Sembunyikan halaman landing page
        self.main_frame.pack()  # Tampilkan kembali halaman pemilihan jenis user

############################################################### STATUS BOOKING PAGE ###############################################################
    def create_status_booking_page_admin(self):
        # Create frame for cek room page
        self.status_booking_page_admin_frame = tk.Frame(
            self.root, padx=20, pady=10)

        # Create header
        header_style = ttk.Style()
        header_style.configure(
            "Header.TLabel", font=("Inter", 20))

        label_header_user = ttk.Label(
            self.status_booking_page_admin_frame, text="Aplikasi Peminjaman Ruangan FEB", style="Header.TLabel"
        )
        label_header_user.grid(row=1, column=0, columnspan=2, pady=40)

        # Create labels
        judul_style = ttk.Style()
        judul_style.configure(
            "Judul.TLabel", font=("Inter", 16))
        label_judul = ttk.Label(
            self.status_booking_page_admin_frame, text="Status Booking Ruangan", style="Judul.TLabel")
        label_judul.grid(row=2, column=0, columnspan=2, pady=20)

        subjudul_style = ttk.Style()
        subjudul_style.configure(
            "Subjudul.TLabel", font=("Inter", 16))
        label_pilih_ruangan = ttk.Label(
            self.status_booking_page_admin_frame, text="Silahkan pilih ruangan!", style="Subjudul.TLabel")
        label_pilih_ruangan.grid(row=3, column=0, columnspan=2, pady=20)

        # Create dropdown for room selection
        self.ruangan_var_status_booking_admin = tk.StringVar()
        self.ruangan_dropdown_status_booking_admin = ttk.Combobox(
            self.status_booking_page_admin_frame, textvariable=self.ruangan_var_status_booking_admin, state='readonly')
        self.ruangan_dropdown_status_booking_admin.grid(
            row=4, column=0, pady=20)

        # Create button to status booking
        check_button_style = ttk.Style()
        check_button_style.configure(
            "Checkbutton.TButton", font=("Inter", 14))
        cek_status_booking = ttk.Button(self.status_booking_page_admin_frame, style="Checkbutton.TButton",
                                        text="Cek Status", command=self.on_cek_status_booking_admin_click)
        cek_status_booking.grid(row=4, column=1, pady=20, padx=(10, 0))

        # Create subframe for additional buttons
        button_subframe = tk.Frame(
            self.status_booking_page_admin_frame, padx=20, pady=20)
        button_subframe.grid(row=5, column=0, columnspan=2, pady=20)

        # Create back button
        button_style = ttk.Style()
        button_style.configure(
            "Button.TButton", font=("Inter", 14))
        back_button = ttk.Button(self.status_booking_page_admin_frame, text="Back", style="Button.TButton",
                                 command=self.on_back_from_status_booking_page_admin_click)
        back_button.grid(row=6, column=0, padx=10, pady=(20, 0))

        # Hide cek room page initially
        self.status_booking_page_admin_frame.pack_forget()

    def update_dropdown_values_status_booking_admin(self):
        # Ambil ruangan dari database dan perbarui nilai dropdown
        query = "SELECT room_name FROM room"
        rooms = self.db.fetch_data(query)
        self.ruangan_dropdown_status_booking_admin['values'] = [
            room[0] for room in rooms]

    def on_cek_status_booking_admin_click(self):
        selected_ruangan = self.ruangan_var_status_booking_admin.get()

        # Query untuk mendapatkan data jadwal peminjaman dengan pengurutan berdasarkan waktu mulai
        query = """
            SELECT
                room.room_name AS NamaRuangan,
                CONCAT(reservation.booker_name, ' - ', reservation.booker_npm, ' - ', reservation.booker_major) AS IdentitasPeminjam,
                CONCAT(reservation.checkin_date, ' -> ', reservation.checkout_date) AS WaktuPeminjaman,
                reservation.approval_status AS StatusBooking,
                reservation.facility_check_status AS StatusFacility
            FROM
                reservation
            JOIN room ON reservation.room_id = room.id
            WHERE
                room.room_name = %s
            ORDER BY
                reservation.checkin_date
        """

        # Eksekusi query dengan parameter ruangan yang dipilih
        data = (selected_ruangan,)
        result = self.db.fetch_data(query, data)

        # Tampilkan hasil query dalam bentuk tabel
        self.display_table_status_booking_admin(result)

        # Create back button
        back_button = ttk.Button(self.status_booking_page_admin_frame, text="Back", style="Button.TButton",
                                 command=self.on_back_from_status_booking_page_admin_click)
        back_button.grid(row=6, column=0, padx=10, pady=(20, 0))

    def display_table_status_booking_admin(self, data):
        # Hapus widget tabel sebelumnya (jika ada)
        for widget in self.cek_room_page_frame.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.pack_forget()

        # Create table frame
        table_frame = tk.Frame(self.status_booking_page_admin_frame)
        table_frame.grid(row=5, column=0, columnspan=2, pady=10)

        # Create Treeview (table) with vertical scrollbar
        columns = ("No", "Nama Ruangan", "Identitas Peminjam",
                   "Waktu Peminjaman", "Status Booking", "Status Fasilitas")
        self.table_booking_admin = ttk.Treeview(
            table_frame, columns=columns, show="headings", height=5)

        # Configure column widths
        column_widths = [50, 150, 200, 150, 150, 150]
        for col, width in zip(columns, column_widths):
            self.table_booking_admin.column(col, width=width, anchor="center")

        # Configure column headings
        for col in columns:
            self.table_booking_admin.heading(col, text=col)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.table_booking_admin.yview)
        self.table_booking_admin.configure(yscrollcommand=scrollbar.set)

        # Pack components
        self.table_booking_admin.pack(side="left")
        scrollbar.pack(side="right", fill="y")

        # Add data to the table
        for i, row in enumerate(data, start=1):
            # Replace None or NULL with '-'
            modified_row = tuple(
                [(col if col is not None else '-') for col in row])
            self.table_booking_admin.insert(
                "", "end", values=(i,) + modified_row)

    def on_back_from_status_booking_page_admin_click(self):
        # Sembunyikan halaman cek room page
        self.status_booking_page_admin_frame.pack_forget()
        self.landing_page_admin_frame.pack()  # Tampilkan kembali halaman landing page

############################################################### KONFIRMASI BOOKING PAGE ###############################################################
    def create_konfirmasi_booking_page_admin(self):
        # Create frame for cek room page
        self.konfirmasi_booking_page_admin_frame = tk.Frame(
            self.root, padx=20, pady=10)

        # Create header
        header_style = ttk.Style()
        header_style.configure(
            "Header.TLabel", font=("Inter", 20))

        label_header_user = ttk.Label(
            self.konfirmasi_booking_page_admin_frame, text="Aplikasi Peminjaman Ruangan FEB", style="Header.TLabel"
        )
        label_header_user.grid(row=1, column=0, columnspan=2, pady=40)

        # Create labels
        judul_style = ttk.Style()
        judul_style.configure(
            "Judul.TLabel", font=("Inter", 16))
        label_judul = ttk.Label(
            self.konfirmasi_booking_page_admin_frame, text="Konfirmasi Booking Ruangan", style="Judul.TLabel")
        label_judul.grid(row=2, column=0, columnspan=2, pady=20)

        subjudul_style = ttk.Style()
        subjudul_style.configure(
            "Subjudul.TLabel", font=("Inter", 16))
        label_pilih_ruangan = ttk.Label(
            self.konfirmasi_booking_page_admin_frame, text="Silahkan pilih ruangan!", style="Subjudul.TLabel")
        label_pilih_ruangan.grid(row=3, column=0, columnspan=2, pady=20)

        # Create dropdown for room selection
        self.ruangan_var_konfirmasi_booking_admin = tk.StringVar()
        self.ruangan_dropdown_konfirmasi_booking_admin = ttk.Combobox(
            self.konfirmasi_booking_page_admin_frame, textvariable=self.ruangan_var_konfirmasi_booking_admin, state='readonly')
        self.ruangan_dropdown_konfirmasi_booking_admin.grid(
            row=4, column=0, pady=20)

        # Create button to status booking
        check_button_style = ttk.Style()
        check_button_style.configure(
            "Checkbutton.TButton", font=("Inter", 14))
        cek_data_konfirmasi_admin = ttk.Button(
            self.konfirmasi_booking_page_admin_frame, text="Cek Data", style="Checkbutton.TButton", command=self.on_cek_data_konfirmasi_admin_click)
        cek_data_konfirmasi_admin.grid(row=4, column=1, pady=20, padx=(10, 0))

        # Create back button
        button_style = ttk.Style()
        button_style.configure(
            "Button.TButton", font=("Inter", 16))
        back_button = ttk.Button(self.konfirmasi_booking_page_admin_frame, style="Button.TButton",
                                 text="Back", command=self.on_back_from_konfirmasi_booking_admin_click)
        back_button.grid(row=6, column=0, pady=20)

        # Hide cek room page initially
        self.konfirmasi_booking_page_admin_frame.pack_forget()

    def update_dropdown_values_konfirmasi_booking_admin(self):
        # Ambil ruangan dari database dan perbarui nilai dropdown
        query = "SELECT room_name FROM room"
        rooms = self.db.fetch_data(query)
        self.ruangan_dropdown_konfirmasi_booking_admin['values'] = [
            room[0] for room in rooms]

    def on_cek_data_konfirmasi_admin_click(self):
        selected_ruangan = self.ruangan_var_konfirmasi_booking_admin.get()

        # Query untuk mendapatkan data jadwal peminjaman dengan pengurutan berdasarkan waktu mulai
        query = """
            SELECT
                reservation.id As ReservationId,
                room.room_name AS NamaRuangan,
                CONCAT(reservation.booker_name, ' - ', reservation.booker_npm, ' - ', reservation.booker_major) AS IdentitasPeminjam,
                CONCAT(reservation.checkin_date, ' -> ', reservation.checkout_date) AS WaktuPeminjaman
            FROM
                reservation
            JOIN room ON reservation.room_id = room.id
            WHERE
                room.room_name = %s
            ORDER BY
                reservation.checkin_date
        """

        # Eksekusi query dengan parameter ruangan yang dipilih
        data = (selected_ruangan,)
        result = self.db.fetch_data(query, data)

        # Tampilkan hasil query dalam bentuk tabel
        self.display_table_konfirmasi_booking_admin(result)

        # Create back button
        back_button = ttk.Button(self.konfirmasi_booking_page_admin_frame, style="Button.TButton",
                                 text="Back", command=self.on_back_from_konfirmasi_booking_admin_click)
        back_button.grid(row=6, column=0, pady=20)

    def display_table_konfirmasi_booking_admin(self, data):
        # Hapus widget tabel sebelumnya (jika ada)
        for widget in self.konfirmasi_booking_page_admin_frame.winfo_children():
            if isinstance(widget, ttk.Treeview):
                widget.pack_forget()

        # Create table frame
        table_frame = tk.Frame(self.konfirmasi_booking_page_admin_frame)
        table_frame.grid(row=5, column=0, columnspan=3, pady=20)

        # Create Treeview (table) with vertical scrollbar
        columns = ("No", "Nama Ruangan", "Identitas Peminjam",
                   "Waktu Peminjaman", "Action")
        self.konfirmasi_booking_admin = ttk.Treeview(
            table_frame, columns=columns, show="headings", height=5)

        # Configure column widths
        column_widths = [50, 100, 200, 150, 100]
        for col, width in zip(columns, column_widths):
            self.konfirmasi_booking_admin.column(
                col, width=width, anchor="center")

        # Configure column headings
        for col in columns:
            self.konfirmasi_booking_admin.heading(col, text=col)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.konfirmasi_booking_admin.yview)
        self.konfirmasi_booking_admin.configure(yscrollcommand=scrollbar.set)

        # Pack components
        self.konfirmasi_booking_admin.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        for i, row in enumerate(data, start=1):
            # Replace None or NULL with '-'
            modified_row = tuple(
                [(col if col is not None else '-') for col in row])
            # Insert data into the table
            values = (i,) + modified_row[1:] + ("detail",)
            item_id = self.konfirmasi_booking_admin.insert(
                "", "end", values=values)

            # Bind the click event to the "detail" action for each row
            self.konfirmasi_booking_admin.tag_configure(
                f"action_button_{i}", background="lightblue")
            self.konfirmasi_booking_admin.tag_bind(
                f"action_button_{i}", "<Button-1>", lambda event, data=modified_row: self.on_detail_informasi_booking_admin_click(data))
            self.konfirmasi_booking_admin.item(
                item_id, tags=(f"action_button_{i}",))

    def on_detail_informasi_booking_admin_click(self, data):
        reservation_id = data[0]

        query = """
            SELECT
                reservation.id AS ReservationId,
                room.id AS RoomId,
                room.room_name AS NamaRuangan,
                reservation.booker_name AS NamaPeminjam, 
                reservation.booker_npm AS NpmPeminjam, 
                reservation.booker_email AS EmailPeminjam, 
                reservation.booker_major AS ProdiPeminjam,
                reservation.booker_phone_number AS NoHpPeminjam,
                CONCAT(reservation.checkin_date, ' -> ', reservation.checkout_date) AS WaktuPeminjaman,
                reservation.approval_status AS ApprovalStatus,
                reservation.facility_check_status AS FacilityStatus
            FROM
                reservation
            JOIN room ON reservation.room_id = room.id
            WHERE
                reservation.id = %s
        """
        data = (reservation_id,)
        result = self.db.fetch_data(query, data)

        # Unpack the result and assign values to the corresponding variables
        (reserv_id, room_id, ruangan, nama, npm, email, prodi, nomor_hp,
         waktu_pinjam, approval_status, facility_status) = result[0]

        # Hide the current page
        self.konfirmasi_booking_page_admin_frame.pack_forget()

        # Show the new form page
        self.form_konfirmasi_admin_page_frame.pack()

        # Set values to the corresponding labels/entries in the form
        self.reservation_id_admin = reserv_id
        self.room_id_admin = room_id
        self.lebel_ruangan_konf_admin.config(text=ruangan)
        self.entry_nama_konf_admin.config(text=nama)
        self.entry_npm_konf_admin.config(text=npm)
        self.entry_email_konf_admin.config(text=email)
        self.entry_prodi_konf_admin.config(text=prodi)
        self.entry_no_hp_konf_admin.config(text=nomor_hp)
        self.entry_waktu_pinjam_konf_admin.config(text=waktu_pinjam)
        self.dropdown_form_konfirmasi_booking_admin.set(approval_status)
        self.status_fasilitas_dropdown.set(facility_status)

    def on_back_from_konfirmasi_booking_admin_click(self):
        self.konfirmasi_booking_page_admin_frame.pack_forget()
        self.landing_page_admin_frame.pack()

############################################################### FORM KONFIRMASI BOOKING PAGE ###############################################################
    def create_form_konfirmasi_admin_page(self):
        self.form_konfirmasi_admin_page_frame = tk.Frame(
            root, padx=20, pady=10)

        # Create header
        header_style = ttk.Style()
        header_style.configure(
            "Header.TLabel", font=("Inter", 20))

        label_header_user = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="Aplikasi Peminjaman Ruangan FEB", style="Header.TLabel"
        )
        label_header_user.grid(row=1, column=0, columnspan=2, pady=40)

        # Create labels
        judul_style = ttk.Style()
        judul_style.configure(
            "Judul.TLabel", font=("Inter", 16))
        label_judul = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="Identitas Booking - Konfirmasi", style="Judul.TLabel")
        label_judul.grid(row=2, column=0, columnspan=2, pady=20)

        # Create form elements
        form_label_style = ttk.Style()
        form_label_style.configure(
            "FormLabel.TLabel", font=("Inter", 12))
        label_ruangan = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="Ruangan", style="FormLabel.TLabel")
        label_ruangan.grid(row=3, column=0, pady=15)

        self.lebel_ruangan_konf_admin = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="")
        self.lebel_ruangan_konf_admin.grid(row=3, column=1, pady=15)

        label_nama = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="Nama Peminjam", style="FormLabel.TLabel")
        label_nama.grid(row=4, column=0, pady=15)

        self.entry_nama_konf_admin = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="")
        self.entry_nama_konf_admin.grid(row=4, column=1, pady=15)

        label_npm = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="NPM Peminjam", style="FormLabel.TLabel")
        label_npm.grid(row=5, column=0, pady=15)

        self.entry_npm_konf_admin = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="")
        self.entry_npm_konf_admin.grid(row=5, column=1, pady=15)

        label_email = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="Email Peminjam", style="FormLabel.TLabel")
        label_email.grid(row=6, column=0, pady=15)

        self.entry_email_konf_admin = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="")
        self.entry_email_konf_admin.grid(row=6, column=1, pady=15)

        label_prodi = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="Prodi Peminjam", style="FormLabel.TLabel")
        label_prodi.grid(row=7, column=0, pady=15)

        self.entry_prodi_konf_admin = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="")
        self.entry_prodi_konf_admin.grid(row=7, column=1, pady=15)

        label_no_hp = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="No HP Peminjam", style="FormLabel.TLabel")
        label_no_hp.grid(row=8, column=0, pady=15)

        self.entry_no_hp_konf_admin = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="")
        self.entry_no_hp_konf_admin.grid(row=8, column=1, pady=15)

        waktu_peminjaman = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="Waktu Peminjaman", style="FormLabel.TLabel")
        waktu_peminjaman.grid(row=9, column=0, pady=15)

        self.entry_waktu_pinjam_konf_admin = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="")
        self.entry_waktu_pinjam_konf_admin.grid(row=9, column=1, pady=15)

        label_status = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="Status", style="FormLabel.TLabel")
        label_status.grid(row=10, column=0, pady=15)

        # Create a list of possible values for the dropdown
        approval_status_values = [
            "Menunggu Persetujuan", "Disetujui", "Ditolak", "Pengecekan Fasilitas", "Selesai"]

        # Initialize StringVar for the dropdown
        self.var_form_konfirmasi_booking_admin = tk.StringVar()

        # Create the dropdown
        self.dropdown_form_konfirmasi_booking_admin = ttk.Combobox(
            self.form_konfirmasi_admin_page_frame,
            textvariable=self.var_form_konfirmasi_booking_admin,
            values=approval_status_values,  # Set the values for the dropdown
            state="readonly"  # Make the dropdown read-only
        )
        self.dropdown_form_konfirmasi_booking_admin.grid(
            row=10, column=1, pady=15)

        # Initialize StringVar for the second dropdown
        self.status_fasilitas_var = tk.StringVar()

        # Function to update the second dropdown based on the first dropdown selection
        def update_status_fasilitas_dropdown(*args):
            selected_status = self.var_form_konfirmasi_booking_admin.get()
            status_fasilitas_values = []

            if selected_status == "Pengecekan Fasilitas":
                status_fasilitas_values = ["Menunggu Pengecekan Fasilitas",
                                           "Fasilitas Rusak", "Menunggu Konfirmasi Penggantian Fasilitas", "Selesai"]

            # Update the values in the second dropdown
            self.status_fasilitas_var.set('')  # Clear the previous selection
            self.status_fasilitas_dropdown["values"] = status_fasilitas_values

        # Trace the change in the first dropdown and call the update function
        self.var_form_konfirmasi_booking_admin.trace_add(
            "write", update_status_fasilitas_dropdown)

        label_status_fasilitas = ttk.Label(
            self.form_konfirmasi_admin_page_frame, text="Fasilitas Status", style="FormLabel.TLabel")
        label_status_fasilitas.grid(row=11, column=0, pady=15)

        # Create the second dropdown
        self.status_fasilitas_dropdown = ttk.Combobox(
            self.form_konfirmasi_admin_page_frame,
            textvariable=self.status_fasilitas_var,
            state="readonly"  # Make the second dropdown read-only
        )
        self.status_fasilitas_dropdown.grid(row=11, column=1, pady=15)

        # Create buttons
        button_style = ttk.Style()
        button_style.configure(
            "Button.TButton", font=("Inter", 16))
        back_button = ttk.Button(self.form_konfirmasi_admin_page_frame, text="Back", style="Button.TButton",
                                 command=self.on_back_from_form_konfirmasi_admin_page_click)
        back_button.grid(row=12, column=0, pady=20)

        simpan_konfirmasi_status_admin_button = ttk.Button(
            self.form_konfirmasi_admin_page_frame, text="Simpan", style="Button.TButton", command=self.on_simpan_konfirmasi_status_admin_button_click)
        simpan_konfirmasi_status_admin_button.grid(row=12, column=1, pady=20)

        # Hide buat booking page initially
        self.form_konfirmasi_admin_page_frame.pack_forget()

    def on_simpan_konfirmasi_status_admin_button_click(self):
        # Get Ids
        reserv_id = self.reservation_id_admin
        room_id = self.room_id_admin

        # Get values from the form
        status = self.var_form_konfirmasi_booking_admin.get()
        f_status = self.status_fasilitas_var.get()

        if status == "Disetujui" or status == "Ditolak":
            # Update reservation status
            query_update_reservation = "UPDATE reservation SET approval_status = %s WHERE id = %s"
            data_update_reservation = (status, reserv_id)
            self.db.execute_query(query_update_reservation,
                                  data_update_reservation)

            messagebox.showinfo("Success", "Berhasil Menyimpan Data!")

            self.form_konfirmasi_admin_page_frame.pack_forget()
            self.konfirmasi_booking_page_admin_frame.pack()
        elif status == "Pengecekan Fasilitas":
            if f_status == "":
                messagebox.showerror("Error", "Pilih Fasilitas Status!")
            elif f_status == "Menunggu Pengecekan Fasilitas":
                # Update reservation status
                query_update_reservation = "UPDATE reservation SET approval_status = %s, facility_check = 0, facility_check_status = %s WHERE id = %s"
                data_update_reservation = (status, f_status, reserv_id)
                self.db.execute_query(
                    query_update_reservation, data_update_reservation)

                messagebox.showinfo("Success", "Berhasil Menyimpan Data!")

                self.form_konfirmasi_admin_page_frame.pack_forget()
                self.konfirmasi_booking_page_admin_frame.pack()
            elif f_status == "Fasilitas Rusak":
                # Check if replacement data already exists
                query_check_replacement = "SELECT id FROM facility_replacement WHERE reservation_id = %s AND room_id = %s"
                data_check_replacement = (reserv_id, room_id)
                existing_replacement = self.db.fetch_data(
                    query_check_replacement, data_check_replacement)

                if existing_replacement:
                    messagebox.showerror(
                        "Error", "Replacement data already exists for this reservation")
                else:
                    # Update status
                    query_update_reservation = "UPDATE reservation SET approval_status = %s, facility_check = 1, facility_check_status = %s WHERE id = %s"
                    data_update_reservation = (status, f_status, reserv_id)
                    self.db.execute_query(
                        query_update_reservation, data_update_reservation)

                    # Insert booking data into the reservation table
                    query_insert_replacement = """
                        INSERT INTO facility_replacement (reservation_id, room_id, replacement_desc, replacement_status)
                        VALUES (%s, %s, %s, %s)
                    """
                    replacement_data = (
                        reserv_id, room_id, '', 'Buat Dokumen Penggantian Fasilitas')
                    self.db.execute_query(
                        query_insert_replacement, replacement_data)

                    messagebox.showinfo("Success", "Berhasil Menyimpan Data!")

                    self.form_konfirmasi_admin_page_frame.pack_forget()
                    self.konfirmasi_booking_page_admin_frame.pack()
            elif f_status == "Selesai":
                query_update_reservation = "UPDATE reservation SET approval_status = %s, facility_check = 1, facility_check_status = %s WHERE id = %s"
                data_update_reservation = ("Selesai", f_status, reserv_id)
                self.db.execute_query(
                    query_update_reservation, data_update_reservation)

                messagebox.showinfo("Success", "Berhasil Menyimpan Data!")

                self.form_konfirmasi_admin_page_frame.pack_forget()
                self.konfirmasi_booking_page_admin_frame.pack()
        elif status == "Selesai":
            query_update_reservation = "UPDATE reservation SET approval_status = %s, facility_check_status = %s WHERE id = %s"
            data_update_reservation = (status, "Selesai", reserv_id)
            self.db.execute_query(query_update_reservation,
                                  data_update_reservation)

            messagebox.showinfo("Success", "Berhasil Menyimpan Data!")

            self.form_konfirmasi_admin_page_frame.pack_forget()
            self.konfirmasi_booking_page_admin_frame.pack()
        else:
            messagebox.showerror("Error", "Pilih Status!")
            return

    def on_back_from_form_konfirmasi_admin_page_click(self):
        # Sembunyikan halaman buat booking page
        self.form_konfirmasi_admin_page_frame.pack_forget()
        # Tampilkan kembali halaman cek room page
        self.konfirmasi_booking_page_admin_frame.pack()


############################################################### RUN APP ###############################################################
if __name__ == '__main__':
    root = tk.Tk()
    app = PeminjamanRuanganApp(root)
    root.mainloop()