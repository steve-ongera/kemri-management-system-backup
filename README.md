# KEMRI Data Management System 🏥

## Overview

This is a Django-based web application designed for managing and analyzing data related to disease testing and research at KEMRI (Kenya Medical Research Institute). The system provides a dynamic dashboard for visualizing key statistics and trends, ensuring data-driven decision-making.


![System Status](https://img.shields.io/badge/status-active-success.svg)
![Django Version](https://img.shields.io/badge/django-latest-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## 📋 Key Features:


-  **Disease Testing Data**: Add and view details of tested diseases, including test counts and trends.
- **Dynamic Data Visualization**: Interactive donut charts and other visualizations to display disease testing statistics.
- **Secure User Authentication**: Role-based access for administrators and staff.
- **Modern Dashboard**: Built with Bootstrap and ECharts for a professional and responsive interface.
- **Recent Activities and Updates**: Stay updated with the latest activities and news within the system.
- **Staff Management**: Comprehensive tracking of doctors, nurses, and administrative staff
- **Patient Care**: Complete patient history and medical records
- **Appointment System**: Efficient scheduling and management
- **Department Organization**: Structured department hierarchy and management
- **Resource Tracking**: Lab tests, reports, and medical documentation

---

## Technologies Used:
- Backend: Django
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Database: SQLite/PostgreSQL
- Charting Library: ECharts
- Others: Python, Django ORM

## 🏗 Architecture

### Primary Models

#### 👨‍⚕️ Medical Staff
| Model | Description |
|-------|-------------|
| `Doctor` | Specialists with department assignments and availability tracking |
| `Intern` | Training medical staff with mentor assignments |
| `Staff` | Administrative and support personnel |
| `NonStaff` | Temporary personnel and visitors |

#### 👤 Patient Care
| Model | Description |
|-------|-------------|
| `Patient` | Comprehensive patient information and history |
| `MedicalRecord` | Detailed visit documentation and treatment plans |
| `Appointment` | Scheduling and visit management |

#### 🏢 Administrative
| Model | Description |
|-------|-------------|
| `Department` | Organizational units with research focus |
| `LabTest` | Diagnostic test tracking |
| `Report` | Medical documentation and file management |

---

## 💾 Data Structure

### Key Relationships

```mermaid
graph TD
    A[Department] --> B[Doctor]
    B --> C[Appointment]
    D[Patient] --> C
    B --> E[MedicalRecord]
    D --> E
    F[Staff] --> A
    G[Intern] --> B
```

### Security Features

- Role-based access control
- Encrypted sensitive data
- Audit logging
- HIPAA compliance measures

---

## 🔧 Technical Specifications

### Requirements

- Django 4.x+
- Python 3.8+
- PostgreSQL/MySQL
- Pillow for image processing

### Key Dependencies

```python
django>=4.0.0
pillow>=9.0.0
django-crispy-forms>=2.0
```

---

## 📁 Model Details

### Doctor Model
- Professional credentials
- Specialization tracking
- Department affiliation
- Availability management

### Patient Model
- Medical history
- Insurance information
- Emergency contacts
- Treatment tracking

### Department Model
- Research specializations
- Staff management
- Resource allocation
- Contact information

### Medical Records
- Visit documentation
- Treatment plans
- Test results
- Prescription tracking

---

## 🔐 Security Implementation

- Data encryption at rest
- Secure file storage
- Access control matrices
- Activity logging
- Regular security audits

---

## 📈 Performance Considerations

- Optimized database queries
- Efficient file handling
- Caching implementations
- Scalable architecture

---

## 🤝 Contributing

Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for detailed contribution guidelines.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.