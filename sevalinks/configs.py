
USER_EDIT_FIELDS = ["first_name", "last_name", "phone_number"]

USER_LOCATION_EDIT_FIELDS = ["user_country", "user_state", "user_area", "user_postcode"]

USER_PROFESSION_EDIT_FIELDS = ["user_profession", "user_job_designation", "user_experience", "user_industry", "user_company", "user_description"]

USER_TYPE = (("ST","STUDENT"), ("PR","PROFESSIONAL"))

INDUSTRY = (("AGRI", "Agriculture"),
            ("BANK", "Banking"),
            ("CONT", "Construction"),
            ("EDU", "Education"),
            ("ENGG", "Engineering"),
            ("FARM", "Farming"),
            ("FOR", "Forestry"),
            ("FIN", "Finance"),
            ("FISH", "Fishing"),
            ("GOV", "Government Services"),
            ("HEAL", "HealthCare"),
            ("INS", "Insurance"),
            ("IT", "IT"),
            ("MDIA", "Media"),
            ("MINE", "Mining"),
            ("NGO", "NGO"),
            ("PHAR", "Pharmaceuticals"),
            ("REAL", "RealEstate"),
            ("SALE", "Sales"),
            ("TRAD", "Trading"),
            ("TRAN", "Transportation"),
            ("OTH", "Others"),)

STATES = (("AP","Andhra Pradesh"),
        ("AR","Arunachal Pradesh"),
        ("AS","Assam"),
        ("BR","Bihar"),
        ("CT","Chhattisgarh"),
        ("GA","Goa"),
        ("GJ","Gujarat"),
        ("HR","Haryana"),
        ("HP","Himachal Pradesh"),
        ("JK","Jammu and Kashmir"),
        ("JH","Jharkhand"),
        ("KA","Karnataka"),
        ("KL","Kerala"),
        ("MP","Madhya Pradesh"),
        ("MH","Maharashtra"),
        ("MN","Manipur"),
        ("ML","Meghalaya"),
        ("MZ","Mizoram"),
        ("NL","Nagaland"),
        ("OR","Odisha"),
        ("PB","Punjab"),
        ("RJ","Rajasthan"),
        ("SK","Sikkim"),
        ("TN","Tamil Nadu"),
        ("TG","Telangana"),
        ("TR","Tripura"),
        ("UT","Uttarakhand"),
        ("UP","Uttar Pradesh"),
        ("WB","West Bengal"),
        ("AN","Andaman and Nicobar Islands"),
        ("CH","Chandigarh"),
        ("DN","Dadra and Nagar Haveli"),
        ("DD","Daman and Diu"),
        ("DL","Delhi"),
        ("LD","Lakshadweep"),
        ("PY","Puducherry"))

DESIGNATION = (("TRAIN", "Trainee"),
               ("ASSO", "Associate"),
               ("SEN", "Senior"),
               ("LEAD", "Lead"),
               ("AMAN", "Assistant Manager"),
               ("MAN", "Manager"),
               ("SMAN", "Senior Manager"),
               ("ADIR", "Associate Director"),
               ("DIR", "Director"),
               ("SDIR", "Senior Director"),
               ("CHAIR", "Chairman"),
               ("MD", "Managing Director"),
               ("CFO", "CFO"),
               ("CTO", "CTO"),
               ("CEO", "CEO"),
               ("OWN", "Owner"))

EXPERIENCE = (("U1","0 - 1 Year"),
              ("U3","1 - 3 Year"),
              ("U6","3 - 6 Year"),
              ("U10","6 - 10 Year"),
              ("U20","10 - 20 Year"),
              ("A20","Above 20 Year"))

NOTIFICATION_CATEGORY = {"0":"/contacts/connections/",
                        "1":"/messages/"}

NOTIFICATION_DESCRIPTION = {"0":"You have a request for Network Connection",
                        "1":"Your request for Network Connection has been accepted"}

NOTIFICATION_DESCRIPTION_TYPE = {"0":"INVITATION",
                        "1":"INVITATION ACCEPT"}
