GRANT ALL PRIVILEGES ON peminjaman_ruangan.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE room (
  id bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  room_name varchar(255) NOT NULL,
  room_location varchar(255) NOT NULL,
  room_facility varchar(255) NOT NULL,
  room_quantity int(3) NOT NULL,
  PRIMARY KEY(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE reservation (
  id bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  room_id bigint(20) NOT NULL,
  booker_name varchar(255) NOT NULL,
  booker_npm varchar(255) NOT NULL,
  booker_email varchar(255) NOT NULL,
  booker_major varchar(255) NOT NULL,
  booker_phone_number varchar(255) NOT NULL,
  checkin_date date NOT NULL,
  checkout_date date NOT NULL,
  approval_status varchar(255) NOT NULL DEFAULT 'Menunggu Persetujuan',
  facility_check TINYINT(1) NULL,
  facility_check_status varchar(255) NULL,
  PRIMARY KEY(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE facility_replacement (
  id bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  reservation_id bigint(20) NOT NULL,
  room_id bigint(20) NOT NULL,
  replacement_desc varchar(255) NOT NULL,
  replacement_status varchar(255) NOT NULL,
  PRIMARY KEY(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO room (room_name, room_location, room_facility, room_quantity) VALUES
('Ruangan 1', 'Gedung A Lantai 1', 'TV, Proyektor, Mic, Speaker', 100),
('Ruangan 2', 'Gedung A Lantai 2', 'Mic, Speaker', 75),
('Ruangan 3', 'Gedung B Lantai 1', 'TV, Proyektor', 50),
('Ruangan 4', 'Gedung B Lantai 2', 'Proyektor', 50),
('Ruangan 5', 'Gedung B Lantai 2', 'TV, Proyektor, Mic, Speaker', 150);