USE [webgiamgia]
GO
/****** Object:  Table [dbo].[ChuongTrinhGiamGia]    Script Date: 22/07/2024 2:32:29 CH ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ChuongTrinhGiamGia](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[tenChuongTrinh] [nvarchar](255) NULL,
	[moTa] [nvarchar](255) NULL,
	[ngayBatDau] [date] NULL,
	[ngayKetThuc] [date] NULL,
	[idNhaCungCap] [int] NULL,
	[isDel] [bit] NULL,
 CONSTRAINT [PK__ChuongTr__3213E83F3B55B68A] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ChuongTrinhYeuThich]    Script Date: 22/07/2024 2:32:29 CH ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ChuongTrinhYeuThich](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[idNguoiDung] [int] NULL,
	[idChuongTrinhGiamGia] [int] NULL,
	[ngayThem] [date] NULL,
	[isDel] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[DanhGia]    Script Date: 22/07/2024 2:32:29 CH ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[DanhGia](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[idNguoiDung] [int] NULL,
	[idChuongTrinhGiamGia] [int] NULL,
	[diemDanhGia] [int] NULL,
	[ngayDanhGia] [date] NULL,
	[isDel] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[LichSuTimKiem]    Script Date: 22/07/2024 2:32:29 CH ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[LichSuTimKiem](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[idNguoiDung] [int] NULL,
	[tuKhoa] [varchar](255) NULL,
	[ngayTimKiem] [date] NULL,
	[isDel] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[MaGiamGia]    Script Date: 22/07/2024 2:32:29 CH ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[MaGiamGia](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[ma] [nvarchar](255) NULL,
	[phanTramGiamGia] [int] NULL,
	[ngayHetHan] [date] NULL,
	[idChuongTrinhGiamGia] [int] NULL,
	[isDel] [bit] NULL,
 CONSTRAINT [PK__MaGiamGi__3213E83FF612C890] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[NguoiDung]    Script Date: 22/07/2024 2:32:29 CH ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[NguoiDung](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[hoTen] [nvarchar](255) NULL,
	[ngaySinh] [date] NULL,
	[diaChi] [nvarchar](255) NULL,
	[soDienThoai] [nvarchar](255) NULL,
	[email] [nvarchar](255) NULL,
	[matKhau] [nvarchar](255) NULL,
	[quyen] [nvarchar](255) NULL,
	[isDel] [bit] NULL,
 CONSTRAINT [PK__NguoiDun__3213E83F577F4010] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[NhaCungCap]    Script Date: 22/07/2024 2:32:29 CH ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[NhaCungCap](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[tenNhaCungCap] [nvarchar](255) NULL,
	[diaChi] [nvarchar](255) NULL,
	[soDienThoai] [nvarchar](255) NULL,
	[email] [nvarchar](255) NULL,
	[isDel] [bit] NULL,
 CONSTRAINT [PK__NhaCungC__3213E83F8BDC83DF] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PhanHoi]    Script Date: 22/07/2024 2:32:29 CH ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PhanHoi](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[idNguoiDung] [int] NULL,
	[idChuongTrinhGiamGia] [int] NULL,
	[noiDung] [nvarchar](255) NULL,
	[ngayPhanHoi] [date] NULL,
	[isDel] [bit] NULL,
 CONSTRAINT [PK__PhanHoi__3213E83F6AF67199] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ThongBao]    Script Date: 22/07/2024 2:32:29 CH ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ThongBao](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[noiDung] [nvarchar](max) NULL,
	[ngayGui] [date] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ThongBao_NguoiDung]    Script Date: 22/07/2024 2:32:29 CH ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ThongBao_NguoiDung](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[idThongBao] [int] NULL,
	[idNguoiDung] [int] NULL,
	[trangThai] [varchar](20) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ThongBaoDaXem]    Script Date: 22/07/2024 2:32:29 CH ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ThongBaoDaXem](
	[idThongBao] [int] NOT NULL,
	[idNguoiDung] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[idThongBao] ASC,
	[idNguoiDung] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [dbo].[ChuongTrinhGiamGia] ON 

INSERT [dbo].[ChuongTrinhGiamGia] ([id], [tenChuongTrinh], [moTa], [ngayBatDau], [ngayKetThuc], [idNhaCungCap], [isDel]) VALUES (1, N'Giám giá mùa hè', N'Giảm 30% cho đơn hàng trên 1 triệu', CAST(N'2024-07-01' AS Date), CAST(N'2024-07-31' AS Date), 1, 0)
INSERT [dbo].[ChuongTrinhGiamGia] ([id], [tenChuongTrinh], [moTa], [ngayBatDau], [ngayKetThuc], [idNhaCungCap], [isDel]) VALUES (2, N'Khuyến mãi đặc biệt', N'GIảm giá 30%', CAST(N'2024-08-01' AS Date), CAST(N'2024-08-15' AS Date), 2, 0)
INSERT [dbo].[ChuongTrinhGiamGia] ([id], [tenChuongTrinh], [moTa], [ngayBatDau], [ngayKetThuc], [idNhaCungCap], [isDel]) VALUES (3, N'Giảm giá Noel', N'Giảm 25%', CAST(N'2024-12-01' AS Date), CAST(N'2024-12-25' AS Date), 3, 0)
INSERT [dbo].[ChuongTrinhGiamGia] ([id], [tenChuongTrinh], [moTa], [ngayBatDau], [ngayKetThuc], [idNhaCungCap], [isDel]) VALUES (4, N'Flash Sale', N'Giảm 50$ trong 2 ngày ', CAST(N'2024-09-15' AS Date), CAST(N'2024-09-16' AS Date), 4, 0)
INSERT [dbo].[ChuongTrinhGiamGia] ([id], [tenChuongTrinh], [moTa], [ngayBatDau], [ngayKetThuc], [idNhaCungCap], [isDel]) VALUES (5, N'Giảm giá tết', N'Giảm 15% trong dịp tết', CAST(N'2024-01-20' AS Date), CAST(N'2024-02-10' AS Date), 5, 0)
SET IDENTITY_INSERT [dbo].[ChuongTrinhGiamGia] OFF
GO
SET IDENTITY_INSERT [dbo].[ChuongTrinhYeuThich] ON 

INSERT [dbo].[ChuongTrinhYeuThich] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [ngayThem], [isDel]) VALUES (1, 1, 1, CAST(N'2024-07-05' AS Date), 0)
INSERT [dbo].[ChuongTrinhYeuThich] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [ngayThem], [isDel]) VALUES (2, 2, 2, CAST(N'2024-08-03' AS Date), 0)
INSERT [dbo].[ChuongTrinhYeuThich] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [ngayThem], [isDel]) VALUES (3, 1, 3, CAST(N'2024-12-10' AS Date), 0)
INSERT [dbo].[ChuongTrinhYeuThich] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [ngayThem], [isDel]) VALUES (4, 2, 4, CAST(N'2024-09-15' AS Date), 0)
INSERT [dbo].[ChuongTrinhYeuThich] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [ngayThem], [isDel]) VALUES (5, 3, 5, CAST(N'2024-01-25' AS Date), 0)
INSERT [dbo].[ChuongTrinhYeuThich] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [ngayThem], [isDel]) VALUES (6, 5, 1, CAST(N'2024-07-22' AS Date), 0)
INSERT [dbo].[ChuongTrinhYeuThich] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [ngayThem], [isDel]) VALUES (7, 5, 3, CAST(N'2024-07-22' AS Date), 1)
SET IDENTITY_INSERT [dbo].[ChuongTrinhYeuThich] OFF
GO
SET IDENTITY_INSERT [dbo].[DanhGia] ON 

INSERT [dbo].[DanhGia] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [diemDanhGia], [ngayDanhGia], [isDel]) VALUES (1, 1, 1, 5, CAST(N'2024-07-15' AS Date), 0)
INSERT [dbo].[DanhGia] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [diemDanhGia], [ngayDanhGia], [isDel]) VALUES (2, 2, 2, 4, CAST(N'2024-08-10' AS Date), 0)
INSERT [dbo].[DanhGia] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [diemDanhGia], [ngayDanhGia], [isDel]) VALUES (3, 1, 3, 3, CAST(N'2024-12-20' AS Date), 0)
INSERT [dbo].[DanhGia] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [diemDanhGia], [ngayDanhGia], [isDel]) VALUES (4, 2, 4, 5, CAST(N'2024-09-17' AS Date), 0)
INSERT [dbo].[DanhGia] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [diemDanhGia], [ngayDanhGia], [isDel]) VALUES (5, 3, 5, 4, CAST(N'2024-02-01' AS Date), 0)
INSERT [dbo].[DanhGia] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [diemDanhGia], [ngayDanhGia], [isDel]) VALUES (6, 5, 4, 5, CAST(N'2024-07-22' AS Date), 0)
SET IDENTITY_INSERT [dbo].[DanhGia] OFF
GO
SET IDENTITY_INSERT [dbo].[LichSuTimKiem] ON 

INSERT [dbo].[LichSuTimKiem] ([id], [idNguoiDung], [tuKhoa], [ngayTimKiem], [isDel]) VALUES (1, 1, N'gi?m giá mùa hè', CAST(N'2024-07-01' AS Date), 0)
INSERT [dbo].[LichSuTimKiem] ([id], [idNguoiDung], [tuKhoa], [ngayTimKiem], [isDel]) VALUES (2, 2, N'khuy?n mãi d?c bi?t', CAST(N'2024-08-01' AS Date), 0)
INSERT [dbo].[LichSuTimKiem] ([id], [idNguoiDung], [tuKhoa], [ngayTimKiem], [isDel]) VALUES (3, 3, N'gi?m giá noel', CAST(N'2024-12-01' AS Date), 0)
INSERT [dbo].[LichSuTimKiem] ([id], [idNguoiDung], [tuKhoa], [ngayTimKiem], [isDel]) VALUES (4, 1, N'flash sale', CAST(N'2024-09-15' AS Date), 0)
INSERT [dbo].[LichSuTimKiem] ([id], [idNguoiDung], [tuKhoa], [ngayTimKiem], [isDel]) VALUES (5, 3, N'gi?m giá t?t', CAST(N'2024-01-20' AS Date), 0)
SET IDENTITY_INSERT [dbo].[LichSuTimKiem] OFF
GO
SET IDENTITY_INSERT [dbo].[MaGiamGia] ON 

INSERT [dbo].[MaGiamGia] ([id], [ma], [phanTramGiamGia], [ngayHetHan], [idChuongTrinhGiamGia], [isDel]) VALUES (1, N'SUMMER20', 20, CAST(N'2024-07-31' AS Date), 1, 0)
INSERT [dbo].[MaGiamGia] ([id], [ma], [phanTramGiamGia], [ngayHetHan], [idChuongTrinhGiamGia], [isDel]) VALUES (2, N'SPECIAL30', 30, CAST(N'2024-08-15' AS Date), 2, 0)
INSERT [dbo].[MaGiamGia] ([id], [ma], [phanTramGiamGia], [ngayHetHan], [idChuongTrinhGiamGia], [isDel]) VALUES (3, N'NOEL25', 25, CAST(N'2024-12-25' AS Date), 3, 0)
INSERT [dbo].[MaGiamGia] ([id], [ma], [phanTramGiamGia], [ngayHetHan], [idChuongTrinhGiamGia], [isDel]) VALUES (4, N'FLASH50', 50, CAST(N'2024-09-16' AS Date), 4, 0)
INSERT [dbo].[MaGiamGia] ([id], [ma], [phanTramGiamGia], [ngayHetHan], [idChuongTrinhGiamGia], [isDel]) VALUES (5, N'TET15', 15, CAST(N'2024-02-10' AS Date), 5, 0)
SET IDENTITY_INSERT [dbo].[MaGiamGia] OFF
GO
SET IDENTITY_INSERT [dbo].[NguoiDung] ON 

INSERT [dbo].[NguoiDung] ([id], [hoTen], [ngaySinh], [diaChi], [soDienThoai], [email], [matKhau], [quyen], [isDel]) VALUES (1, N'Nguyen Van A', CAST(N'1990-01-01' AS Date), N'HCM', N'0901234567', N'1@gmail.com', N'6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', N'khachhang', 0)
INSERT [dbo].[NguoiDung] ([id], [hoTen], [ngaySinh], [diaChi], [soDienThoai], [email], [matKhau], [quyen], [isDel]) VALUES (2, N'Tran Thi B', CAST(N'1992-02-02' AS Date), N'HCM', N'0912345678', N'2@gmail.com', N'6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', N'khachhang', 0)
INSERT [dbo].[NguoiDung] ([id], [hoTen], [ngaySinh], [diaChi], [soDienThoai], [email], [matKhau], [quyen], [isDel]) VALUES (3, N'Le Van C', CAST(N'1994-03-03' AS Date), N'HCM', N'0923456789', N'3@gmail.com', N'6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', N'khachhang', 0)
INSERT [dbo].[NguoiDung] ([id], [hoTen], [ngaySinh], [diaChi], [soDienThoai], [email], [matKhau], [quyen], [isDel]) VALUES (4, N'Pham Thi D', CAST(N'1996-04-04' AS Date), N'HCM', N'0934567890', N'4@gmail.com', N'6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', N'khachhang', 0)
INSERT [dbo].[NguoiDung] ([id], [hoTen], [ngaySinh], [diaChi], [soDienThoai], [email], [matKhau], [quyen], [isDel]) VALUES (5, N'Nguyễn Minh Hòa', CAST(N'2002-07-22' AS Date), N'HCM', N'0353803490', N'hoahuit@gmail.com', N'6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', N'admin', 0)
SET IDENTITY_INSERT [dbo].[NguoiDung] OFF
GO
SET IDENTITY_INSERT [dbo].[NhaCungCap] ON 

INSERT [dbo].[NhaCungCap] ([id], [tenNhaCungCap], [diaChi], [soDienThoai], [email], [isDel]) VALUES (1, N'Shopee', N'HCM', N'0912345678', N'contact@abc.com', 0)
INSERT [dbo].[NhaCungCap] ([id], [tenNhaCungCap], [diaChi], [soDienThoai], [email], [isDel]) VALUES (2, N'Grab', N'HCM', N'0923456789', N'contact@xyz.com', 0)
INSERT [dbo].[NhaCungCap] ([id], [tenNhaCungCap], [diaChi], [soDienThoai], [email], [isDel]) VALUES (3, N'Gojek', N'HCM', N'0934567890', N'contact@def.com', 0)
INSERT [dbo].[NhaCungCap] ([id], [tenNhaCungCap], [diaChi], [soDienThoai], [email], [isDel]) VALUES (4, N'Bee', N'HCM', N'0945678901', N'contact@ghi.com', 0)
INSERT [dbo].[NhaCungCap] ([id], [tenNhaCungCap], [diaChi], [soDienThoai], [email], [isDel]) VALUES (5, N'Momo', N'HCM', N'0956789012', N'contact@jkl.com', 0)
SET IDENTITY_INSERT [dbo].[NhaCungCap] OFF
GO
SET IDENTITY_INSERT [dbo].[PhanHoi] ON 

INSERT [dbo].[PhanHoi] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [noiDung], [ngayPhanHoi], [isDel]) VALUES (1, 1, 1, N'Quá tệ', CAST(N'2024-07-10' AS Date), 0)
INSERT [dbo].[PhanHoi] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [noiDung], [ngayPhanHoi], [isDel]) VALUES (2, 2, 2, N'Hấp dẫn', CAST(N'2024-08-05' AS Date), 0)
INSERT [dbo].[PhanHoi] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [noiDung], [ngayPhanHoi], [isDel]) VALUES (3, 3, 3, N'Quá tuyệt vời', CAST(N'2024-12-15' AS Date), 0)
INSERT [dbo].[PhanHoi] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [noiDung], [ngayPhanHoi], [isDel]) VALUES (4, 2, 4, N'Flash sale quá tuyệt', CAST(N'2024-09-16' AS Date), 0)
INSERT [dbo].[PhanHoi] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [noiDung], [ngayPhanHoi], [isDel]) VALUES (5, 1, 5, N'Khuyến mãi tốt', CAST(N'2024-02-05' AS Date), 0)
INSERT [dbo].[PhanHoi] ([id], [idNguoiDung], [idChuongTrinhGiamGia], [noiDung], [ngayPhanHoi], [isDel]) VALUES (6, 5, 4, N'ok đó', CAST(N'2024-07-22' AS Date), 0)
SET IDENTITY_INSERT [dbo].[PhanHoi] OFF
GO
SET IDENTITY_INSERT [dbo].[ThongBao] ON 

INSERT [dbo].[ThongBao] ([id], [noiDung], [ngayGui]) VALUES (1, N'Chương trình đã bắt đầu', CAST(N'2024-07-01' AS Date))
INSERT [dbo].[ThongBao] ([id], [noiDung], [ngayGui]) VALUES (2, N' dành cho khách hàng VIP!', CAST(N'2024-08-01' AS Date))
INSERT [dbo].[ThongBao] ([id], [noiDung], [ngayGui]) VALUES (3, N'Giảm giá đã diễn ra', CAST(N'2024-12-01' AS Date))
INSERT [dbo].[ThongBao] ([id], [noiDung], [ngayGui]) VALUES (4, N'Flash sale 50% ', CAST(N'2024-09-15' AS Date))
INSERT [dbo].[ThongBao] ([id], [noiDung], [ngayGui]) VALUES (5, N'Chuong trình ', CAST(N'2024-01-20' AS Date))
SET IDENTITY_INSERT [dbo].[ThongBao] OFF
GO
SET IDENTITY_INSERT [dbo].[ThongBao_NguoiDung] ON 

INSERT [dbo].[ThongBao_NguoiDung] ([id], [idThongBao], [idNguoiDung], [trangThai]) VALUES (1, 1, 1, N'chuaDoc')
INSERT [dbo].[ThongBao_NguoiDung] ([id], [idThongBao], [idNguoiDung], [trangThai]) VALUES (2, 2, 2, N'chuaDoc')
INSERT [dbo].[ThongBao_NguoiDung] ([id], [idThongBao], [idNguoiDung], [trangThai]) VALUES (3, 3, 2, N'chuaDoc')
INSERT [dbo].[ThongBao_NguoiDung] ([id], [idThongBao], [idNguoiDung], [trangThai]) VALUES (4, 4, 3, N'chuaDoc')
INSERT [dbo].[ThongBao_NguoiDung] ([id], [idThongBao], [idNguoiDung], [trangThai]) VALUES (5, 5, 1, N'chuaDoc')
INSERT [dbo].[ThongBao_NguoiDung] ([id], [idThongBao], [idNguoiDung], [trangThai]) VALUES (6, 1, 5, N'daDoc')
SET IDENTITY_INSERT [dbo].[ThongBao_NguoiDung] OFF
GO
INSERT [dbo].[ThongBaoDaXem] ([idThongBao], [idNguoiDung]) VALUES (1, 1)
INSERT [dbo].[ThongBaoDaXem] ([idThongBao], [idNguoiDung]) VALUES (2, 1)
INSERT [dbo].[ThongBaoDaXem] ([idThongBao], [idNguoiDung]) VALUES (3, 1)
INSERT [dbo].[ThongBaoDaXem] ([idThongBao], [idNguoiDung]) VALUES (4, 1)
INSERT [dbo].[ThongBaoDaXem] ([idThongBao], [idNguoiDung]) VALUES (5, 1)
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__MaGiamGi__3213C8B6665626A9]    Script Date: 22/07/2024 2:32:30 CH ******/
ALTER TABLE [dbo].[MaGiamGia] ADD  CONSTRAINT [UQ__MaGiamGi__3213C8B6665626A9] UNIQUE NONCLUSTERED 
(
	[ma] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [UQ__NguoiDun__AB6E61647B0B9B8D]    Script Date: 22/07/2024 2:32:30 CH ******/
ALTER TABLE [dbo].[NguoiDung] ADD  CONSTRAINT [UQ__NguoiDun__AB6E61647B0B9B8D] UNIQUE NONCLUSTERED 
(
	[email] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[ChuongTrinhGiamGia] ADD  CONSTRAINT [DF__ChuongTri__isDel__48CFD27E]  DEFAULT ((0)) FOR [isDel]
GO
ALTER TABLE [dbo].[ChuongTrinhYeuThich] ADD  DEFAULT ((0)) FOR [isDel]
GO
ALTER TABLE [dbo].[DanhGia] ADD  DEFAULT ((0)) FOR [isDel]
GO
ALTER TABLE [dbo].[LichSuTimKiem] ADD  DEFAULT ((0)) FOR [isDel]
GO
ALTER TABLE [dbo].[MaGiamGia] ADD  CONSTRAINT [DF__MaGiamGia__isDel__4CA06362]  DEFAULT ((0)) FOR [isDel]
GO
ALTER TABLE [dbo].[NguoiDung] ADD  CONSTRAINT [DF__NguoiDung__isDel__4D94879B]  DEFAULT ((0)) FOR [isDel]
GO
ALTER TABLE [dbo].[NhaCungCap] ADD  CONSTRAINT [DF__NhaCungCa__isDel__4E88ABD4]  DEFAULT ((0)) FOR [isDel]
GO
ALTER TABLE [dbo].[PhanHoi] ADD  CONSTRAINT [DF__PhanHoi__isDel__4F7CD00D]  DEFAULT ((0)) FOR [isDel]
GO
ALTER TABLE [dbo].[ThongBao_NguoiDung] ADD  DEFAULT ('chuaDoc') FOR [trangThai]
GO
ALTER TABLE [dbo].[ChuongTrinhGiamGia]  WITH CHECK ADD  CONSTRAINT [FK__ChuongTri__idNha__5165187F] FOREIGN KEY([idNhaCungCap])
REFERENCES [dbo].[NhaCungCap] ([id])
GO
ALTER TABLE [dbo].[ChuongTrinhGiamGia] CHECK CONSTRAINT [FK__ChuongTri__idNha__5165187F]
GO
ALTER TABLE [dbo].[ChuongTrinhYeuThich]  WITH CHECK ADD  CONSTRAINT [FK__ChuongTri__idChu__52593CB8] FOREIGN KEY([idChuongTrinhGiamGia])
REFERENCES [dbo].[ChuongTrinhGiamGia] ([id])
GO
ALTER TABLE [dbo].[ChuongTrinhYeuThich] CHECK CONSTRAINT [FK__ChuongTri__idChu__52593CB8]
GO
ALTER TABLE [dbo].[ChuongTrinhYeuThich]  WITH CHECK ADD  CONSTRAINT [FK__ChuongTri__idNgu__534D60F1] FOREIGN KEY([idNguoiDung])
REFERENCES [dbo].[NguoiDung] ([id])
GO
ALTER TABLE [dbo].[ChuongTrinhYeuThich] CHECK CONSTRAINT [FK__ChuongTri__idNgu__534D60F1]
GO
ALTER TABLE [dbo].[DanhGia]  WITH CHECK ADD  CONSTRAINT [FK__DanhGia__idChuon__5441852A] FOREIGN KEY([idChuongTrinhGiamGia])
REFERENCES [dbo].[ChuongTrinhGiamGia] ([id])
GO
ALTER TABLE [dbo].[DanhGia] CHECK CONSTRAINT [FK__DanhGia__idChuon__5441852A]
GO
ALTER TABLE [dbo].[DanhGia]  WITH CHECK ADD  CONSTRAINT [FK__DanhGia__idNguoi__5535A963] FOREIGN KEY([idNguoiDung])
REFERENCES [dbo].[NguoiDung] ([id])
GO
ALTER TABLE [dbo].[DanhGia] CHECK CONSTRAINT [FK__DanhGia__idNguoi__5535A963]
GO
ALTER TABLE [dbo].[LichSuTimKiem]  WITH CHECK ADD  CONSTRAINT [FK__LichSuTim__idNgu__5629CD9C] FOREIGN KEY([idNguoiDung])
REFERENCES [dbo].[NguoiDung] ([id])
GO
ALTER TABLE [dbo].[LichSuTimKiem] CHECK CONSTRAINT [FK__LichSuTim__idNgu__5629CD9C]
GO
ALTER TABLE [dbo].[MaGiamGia]  WITH CHECK ADD  CONSTRAINT [FK__MaGiamGia__idChu__571DF1D5] FOREIGN KEY([idChuongTrinhGiamGia])
REFERENCES [dbo].[ChuongTrinhGiamGia] ([id])
GO
ALTER TABLE [dbo].[MaGiamGia] CHECK CONSTRAINT [FK__MaGiamGia__idChu__571DF1D5]
GO
ALTER TABLE [dbo].[PhanHoi]  WITH CHECK ADD  CONSTRAINT [FK__PhanHoi__idChuon__5812160E] FOREIGN KEY([idChuongTrinhGiamGia])
REFERENCES [dbo].[ChuongTrinhGiamGia] ([id])
GO
ALTER TABLE [dbo].[PhanHoi] CHECK CONSTRAINT [FK__PhanHoi__idChuon__5812160E]
GO
ALTER TABLE [dbo].[PhanHoi]  WITH CHECK ADD  CONSTRAINT [FK__PhanHoi__idNguoi__59063A47] FOREIGN KEY([idNguoiDung])
REFERENCES [dbo].[NguoiDung] ([id])
GO
ALTER TABLE [dbo].[PhanHoi] CHECK CONSTRAINT [FK__PhanHoi__idNguoi__59063A47]
GO
ALTER TABLE [dbo].[ThongBao_NguoiDung]  WITH CHECK ADD FOREIGN KEY([idNguoiDung])
REFERENCES [dbo].[NguoiDung] ([id])
GO
ALTER TABLE [dbo].[ThongBao_NguoiDung]  WITH CHECK ADD FOREIGN KEY([idThongBao])
REFERENCES [dbo].[ThongBao] ([id])
GO
ALTER TABLE [dbo].[ThongBaoDaXem]  WITH CHECK ADD FOREIGN KEY([idNguoiDung])
REFERENCES [dbo].[NguoiDung] ([id])
GO
ALTER TABLE [dbo].[ThongBaoDaXem]  WITH CHECK ADD FOREIGN KEY([idThongBao])
REFERENCES [dbo].[ThongBao] ([id])
GO
