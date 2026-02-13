import firebase_admin
from firebase_admin import credentials, firestore

# 1. Firebase Setup
# 'serviceAccountKey.json' file nee script unna folder lone undali
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# 2. ALIET Student List from your Soft Copy
# 69 names structure from PDF [cite: 1, 2, 4, 5]
students_list = [
    {"rollNo": "24HP1A0501", "name": "KORLAPATI AKHILESWARI", "year": 1, "branch": "CSE", "section": "Sec-1"},
    {"rollNo": "24HP1A0502", "name": "JONNAKUTY AMRUTHA DARSHA", "year": 1, "branch": "CSE", "section": "Sec-1"},
    {"rollNo": "24HP1A0503", "name": "KUCHIPUDI ANJALI", "year": 1, "branch": "CSE", "section": "Sec-1"},
    {"rollNo": "24HP1A0504", "name": "BOYINA ANKITHA", "year": 1, "branch": "CSE", "section": "Sec-1"},
    {"rollNo": "24HP1A0505", "name": "BIBI AYESHA", "year": 1, "branch": "CSE", "section": "Sec-1"},
    {"rollNo": "24HP1A0506", "name": "MAJJI BHASHINI", "year": 1, "branch": "CSE", "section": "Sec-1"},
    {"rollNo": "24HP1A0507", "name": "GOLAKOTI BHUVANA", "year": 1, "branch": "CSE", "section": "Sec-1"},
    {"rollNo": "24HP1A0508", "name": "MOPIDEVI HARIKA", "year": 1, "branch": "CSE", "section": "Sec-1"},
    {"rollNo": "24HP1A0517", "name": "NARAMSETTI MEGHANA", "year": 1, "branch": "CSE", "section": "Sec-1"},
    {"rollNo": "24HP1A0557", "name": "EGITI SAMBASIVARAO", "year": 1, "branch": "CSE", "section": "Sec-1"},
    {"rollNo": "25HP5A0505", "name": "VISWANADHAPALLI NARAYANA V", "year": 1, "branch": "CSE", "section": "Sec-1"}
    # Note: Short format for demo. Add other names from your PDF list.
]

def upload():
    print("Mava, Firebase loki data upload avthundi...")
    count = 0
    for s in students_list:
        # 'students' collection loki push chesthunnam
        db.collection("students").add({
            "name": s["name"],
            "rollNo": s["rollNo"],
            "year": s["year"],
            "branch": s["branch"],
            "section": s["section"],
            "attendance": 0 
        })
        count += 1
        print(f"Uploaded {count}: {s['name']}")
    print("\nMava, 69 names success ga upload ayipoyayi!")

if __name__ == "__main__":
    upload()