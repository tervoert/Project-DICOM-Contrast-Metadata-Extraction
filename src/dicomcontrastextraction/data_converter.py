"""
data_converter.py:
    Part of the example dicom2sphn package.
    It contains the DataConverter class, which handles data conversion.
"""

from typing import ClassVar, ReadOnly


#
# Edwin 2026-09-25
#
class DataConverter:
    """
    A class to handle data conversion.
    """

    #
    # Edwin 2026-09-25
    #
    def __init__(self):
        """
        Initializes the DataConverter instance.
        """

    #
    # Body Part Examined
    #

    # The DICOM BodyPartExamined tag value uses DICOM defined terms which should be converted to SNOMED-CT codes for SPHN

    # The newer DICOM tags: 
    # - Anatomic Region Sequence (0008,2218) or 
    # - Primary Anatomic Structure Sequence (0008,2228)
    # already use the indicated SNOMED-CT codes, so this dictionary is only needed for the older BodyPartExamined tag (0018,0015)
    #

    # A dictionary mapping DICOM BodyPartExamined tag values to corresponding SNOMED-CT codes for SPHN
    # Key: DICOM BodyPartExamined tag value (e.g. "ABDOMEN")
    # Value: corresponding SNOMED-CT code (e.g. "818981001")
    # Note: The indicated SNOMED-CT human-readable descriptions are from DICOM and may not be the same as the official SNOMED-CT descriptions
    # Link:https://dicom.nema.org/medical/dicom/current/output/chtml/part16/chapter_L.html
    dicom_body_part_examined_terms_dict: ClassVar[ReadOnly[dict[str, tuple[str,str,str]]]] = {
        "ABDOMEN":          ("SNOMED", "818981001",  "| Abdomen |"),
        "ABDOMENPELVIS":    ("SNOMED", "818982008",  "| Abdomen and Pelvis |"),
        "ABDOMINALAORTA":   ("SNOMED", "7832008",    "| Abdominal aorta |"),
        "ACJOINT":          ("SNOMED", "85856004",   "| Acromioclavicular joint |"),
        "ADRENAL":          ("SNOMED", "23451007",   "| Adrenal gland |"),
        "AMNIOTICFLUID":    ("SNOMED", "77012006",   "| Amniotic fluid |"),
        "ANKLE":            ("SNOMED", "70258002",   "| Ankle joint |"),
        #                   ("SNOMED", "128585006",  "| Anomalous pulmonary vein |"),
        "ANTECUBITALV":     ("SNOMED", "128553008",  "| Antecubital vein |"),
        "ANTCARDIACV":      ("SNOMED", "194996006",  "| Anterior cardiac vein |"),
        "ACA":              ("SNOMED", "60176003",   "| Anterior cerebral artery |"),
        "ANTCOMMA":         ("SNOMED", "8012006",    "| Anterior communicating artery |"),
        "ANTSPINALA":       ("SNOMED", "17388009",   "| Anterior spinal artery |"),
        "ANTTIBIALA":       ("SNOMED", "68053000",   "| Anterior tibial artery |"),
        #                   ("SNOMED", "53505006",   "| Anus |"),
        "ANUSRECTUMSIGMD":  ("SNOMED", "110612005",  "| Anus, rectum and sigmoid colon |"),
        "AORTA":            ("SNOMED", "15825003",   "| Aorta |"),
        "AORTICARCH":       ("SNOMED", "57034009",   "| Aortic arch |"),
        #                   ("SNOMED", "128551005",  "| Aortic fistula |"),
        #                   ("SNOMED", "128564006",  "| Apex of left ventricle |"),
        #                   ("SNOMED", "86598002",   "| Apex of Lung |"),
        #                   ("SNOMED", "128565007",  "| Apex of right ventricle |"),
        "APPENDIX":         ("SNOMED", "66754008",   "| Appendix |"),
        "ARTERY":           ("SNOMED", "51114001",   "| Artery |"),
        "ASCAORTA":         ("SNOMED", "54247002",   "| Ascending aorta |"),
        "ASCENDINGCOLON":   ("SNOMED", "9040008",    "| Ascending colon |"),
        #                   ("SNOMED", "59652004",   "| Atrium |"),
        "AXILLA":           ("SNOMED", "91470000",   "| Axilla |"),
        "AXILLARYA":        ("SNOMED", "67937003",   "| Axillary Artery |"),
        "AXILLARYV":        ("SNOMED", "68705008",   "| Axillary vein |"),
        "AZYGOSVEIN":       ("SNOMED", "72107004",   "| Azygos vein |"),
        "BACK":             ("SNOMED", "77568009",   "| Back |"),
        #                   ("SNOMED", "128981007",  "| Baffle |"),
        "ASILARA":          ("SNOMED", "59011009",   "| Basilar artery |"),
        "BILEDUCT":         ("SNOMED", "28273000",   "| Bile duct |"),
        "BILIARYTRACT":     ("SNOMED", "34707002",   "| Biliary tract |"),
        "BLADDER":          ("SNOMED", "89837001",   "| Bladder |"),
        "BLADDERURETHRA":   ("SNOMED", "110837003",  "| Bladder and urethra |"),
        #                   ("SNOMED", "91830000",   "| Body conduit |"),
        #                   ("SNOMED", "72001000",   "| Bone of lower limb |"),
        #                   ("SNOMED", "371195002",  "| Bone of upper limb |"),
        #                   ("SNOMED", "128548003",  "| Boyd's perforating vein |"),
        "BRACHIALA":        ("SNOMED", "17137000",   "| Brachial artery |"),
        "BRACHIALV":        ("SNOMED", "20115005",   "| Brachial vein |"),
        "BRAIN":            ("SNOMED", "12738006",   "| Brain |"),
        "BREAST":           ("SNOMED", "76752008",   "| Breast |"),
        #                   ("SNOMED", "34411009",   "| Broad ligament |"),
        "BRONCHUS":         ("SNOMED", "955009",     "| Bronchus |"),
        #                   ("SNOMED", "60819002",   "| Buccal region of face |"),
        "BUTTOCK":          ("SNOMED", "46862004",   "| Buttock |"),
        "CALCANEUS":        ("SNOMED", "80144004",   "| Calcaneus |"),
        "CALF":             ("SNOMED", "53840002",   "| Calf of leg |"),
        #                   ("SNOMED", "2334006",    "| Calyx |"),
        "CAROTID":          ("SNOMED", "69105007",   "| Carotid Artery |"),
        "BULB":             ("SNOMED", "21479005",   "| Carotid bulb |"),
        "CELIACA":          ("SNOMED", "57850000",   "| Celiac artery |"),
        "CEPHALICV":        ("SNOMED", "20699002",   "| Cephalic vein |"),
        "CEREBELLUM":       ("SNOMED", "113305005",  "| Cerebellum |"),
        "CEREBRALA":        ("SNOMED", "88556005",   "| Cerebral artery |"),
        "CEREBHEMISPHERE":  ("SNOMED", "372073000",  "| Cerebral hemisphere |"),
        "CSPINE":           ("SNOMED", "122494005",  "| Cervical spine |"),
        "CTSPINE":          ("SNOMED", "1217257000", "| Cervico-thoracic spine |"),
        "CERVIX":           ("SNOMED", "71252005",   "| Cervix |"),
        "CHEEK":            ("SNOMED", "60819002",   "| Cheek |"),
        "CHEST":            ("SNOMED", "43799004",   "| Chest |"),
        "CHESTABDPELVIS":   ("SNOMED", "416775004",  "| Chest, Abdomen and Pelvis |"),
        "CHESTABDOMEN":     ("SNOMED", "416550000",  "| Chest and Abdomen |"),
        "CHOROIDPLEXUS":    ("SNOMED", "80621003",   "| Choroid plexus |"),
        "CIRCLEOFWILLIS":   ("SNOMED", "11279006",   "| Circle of Willis |"),
        "CLAVICLE":         ("SNOMED", "51299004",   "| Clavicle |"),
        "COCCYX":           ("SNOMED", "64688005",   "| Coccyx |"),
        "COLON":            ("SNOMED", "71854001",   "| Colon |"),
        #                   ("SNOMED", "253276007",  "| Common atrium |"),
        "COMMONBILEDUCT":   ("SNOMED", "79741001",   "| Common bile duct |"),
        "CCA":              ("SNOMED", "32062004",   "| Common carotid artery |"),
        "CFA":              ("SNOMED", "181347005",  "| Common femoral artery |"),
        "CFV":              ("SNOMED", "397363009",  "| Common femoral vein |"),
        "COMILIACA":        ("SNOMED", "73634005",   "| Common iliac artery |"),
        "COMILIACV":        ("SNOMED", "46027005",   "| Common iliac vein |"),
        #                   ("SNOMED", "45503006",   "| Common ventricle |"),
        #                   ("SNOMED", "128555001",  "| Congenital coronary artery fistula to left atrium |"),
        #                   ("SNOMED", "128556000",  "| Congenital coronary artery fistula to left ventricle |"),
        #                   ("SNOMED", "128557009",  "| Congenital coronary artery fistula to right atrium |"),
        #                   ("SNOMED", "128558004",  "| Congenital coronary artery fistula to right ventricle |"),
        #                   ("SNOMED", "111289009",  "| Pulmonary arteriovenous fistula |"),
        "CORNEA":           ("SNOMED", "28726007",   "| Cornea |"),
        "CORONARYARTERY":   ("SNOMED", "41801008",   "| Coronary artery |"),
        "CORONARYSINUS":    ("SNOMED", "90219004",   "| Coronary sinus |"),
        #                   ("SNOMED", "128320002",  "| Cranial venous system |"),
        "DESCAORTA":        ("SNOMED", "281130003",  "| Descending aorta |"),
        "DESCENDINGCOLON":  ("SNOMED", "32622004",   "| Descending colon |"),
        #                   ("SNOMED", "128554002",  "| Dodd's perforating vein |"),
        "DUODENUM":         ("SNOMED", "38848004",   "| Duodenum |"),
        "EAR":              ("SNOMED", "117590005",  "| Ear |"),
        "ELBOW":            ("SNOMED", "16953009",   "| Elbow joint |"),
        "ENDOARTERIAL":     ("SNOMED", "51114001",   "| Endo-arterial |"),
        "ENDOCARDIAC":      ("SNOMED", "80891009",   "| Endo-cardiac |"),
        "ENDOESOPHAGEAL":   ("SNOMED", "32849002",   "| Endo-esophageal |"),
        "ENDOMETRIUM":      ("SNOMED", "2739003",    "| Endometrium |"),
        "ENDONASAL":        ("SNOMED", "53342003",   "| Endo-nasal |"),
        "ENDONASOPHARYNYX": ("SNOMED", "18962004",   "| Endo-nasopharyngeal |"),
        "ENDORECTAL":       ("SNOMED", "34402009",   "| Endo-rectal |"),
        "ENDORENAL":        ("SNOMED", "64033007",   "| Endo-renal |"),
        "ENDOURETERIC":     ("SNOMED", "87953007",   "| Endo-ureteric |"),
        "ENDOURETHRAL":     ("SNOMED", "13648007",   "| Endo-urethral |"),
        "ENDOVAGINAL":      ("SNOMED", "76784001",   "| Endo-vaginal |"),
        "ENDOVASCULAR":     ("SNOMED", "59820001",   "| Endo-vascular |"),
        "ENDOVENOUS":       ("SNOMED", "29092000",   "| Endo-venous |"),
        "ENDOVESICAL":      ("SNOMED", "48367006",   "| Endo-vesical |"),
        "WHOLEBODY":        ("SNOMED", "38266002",   "| Entire body |"),
        "EPIDIDYMIS":       ("SNOMED", "87644002",   "| Epididymis |"),
        "EPIGASTRIC":       ("SNOMED", "27947004",   "| Epigastric region |"),
        "ESOPHAGUS":        ("SNOMED", "32849002",   "| Esophagus |"),
        #                   ("SNOMED", "110861005",  "| Esophagus, stomach and duodenum |"),
        "EAC":              ("SNOMED", "84301002",   "| External auditory canal |"),
        "ECA":              ("SNOMED", "22286001",   "| External carotid artery |"),
        "EXTILIACA":        ("SNOMED", "113269004",  "| External iliac artery |"),
        "EXTILIACV":        ("SNOMED", "63507001",   "| External iliac vein |"),
        "EXTJUGV":          ("SNOMED", "71585003",   "| External jugular vein |"),
        "EXTREMITY":        ("SNOMED", "66019005",   "| Extremity |"),
        "EYE":              ("SNOMED", "81745001",   "| Eye |"),
        "EYELID":           ("SNOMED", "80243003",   "| Eyelid |"),
        #                   ("SNOMED", "371398005",  "| Eye region |"),
        "FACE":             ("SNOMED", "89545001",   "| Face |"),
        "FACIALA":          ("SNOMED", "23074001",   "| Facial artery |"),
        #                   ("SNOMED", "91397008",   "| Facial bones |"),
        "FEMORALA":         ("SNOMED", "7657000",    "| Femoral artery |"),
        "FEMORALV":         ("SNOMED", "83419000",   "| Femoral vein |"),
        "FEMUR":            ("SNOMED", "71341001",   "| Femur |"),
        #FETALARM		Fetal arm
        #FETALDIGIT		Fetal digit
        #FETALHEART		Fetal heart
        #FETALLEG		Fetal leg
        #FETALPOLE		Fetal pole
        "FIBULA":           ("SNOMED", "87342007",   "| Fibula |"),
        "FINGER":           ("SNOMED", "7569003",    "| Finger |"),
        "FLANK":            ("SNOMED", "58602004",   "| Flank |"),
        "FONTANEL":         ("SNOMED", "79361005",   "| Fontanel of skull |"),
        "FOOT":             ("SNOMED", "56459004",   "| Foot |"),
        "FOREARM":          ("SNOMED", "14975008",   "| Forearm |"),
        "4THVENTRICLE":     ("SNOMED", "35918002",   "| Fourth ventricle |"),
        "GALLBLADDER":      ("SNOMED", "28231008",   "| Gallbladder |"),
        "GASTRICV":         ("SNOMED", "110568007",  "| Gastric vein |"),
        "GENICULARA":       ("SNOMED", "128559007",  "| Genicular artery |"),
        "GESTSAC":          ("SNOMED", "300571009",  "| Gestational sac |"),
        "GLUTEAL":          ("SNOMED", "46862004",   "| Gluteal region |"),
        #                   ("SNOMED", "5928000",    "| Great cardiac vein |"),
        "GSV":              ("SNOMED", "60734001",   "| Great saphenous vein |"),
        "HAND":             ("SNOMED", "85562004",   "| Hand |"),
        "HEAD":             ("SNOMED", "69536005",   "| Head |"),
        "HEADNECK":         ("SNOMED", "774007",     "| Head and Neck |"),
        "HEART":            ("SNOMED", "80891009",   "| Heart |"),
        "HEPATICA":         ("SNOMED", "76015000",   "| Hepatic artery |"),
        "HEPATICV":         ("SNOMED", "8993003",    "| Hepatic vein |"),
        "HIP":              ("SNOMED", "24136001",   "| Hip joint |"),
        "HUMERUS":          ("SNOMED", "85050009",   "| Humerus |"),
        #                   ("SNOMED", "128560002",  "| Hunterian perforating vein |"),
        "HYPOGASTRIC":      ("SNOMED", "11708003",   "| Hypogastric region |"),
        "HYPOPHARYNX":      ("SNOMED", "81502006",   "| Hypopharynx |"),
        "ILEUM":            ("SNOMED", "34516001",   "| Ileum |"),
        #                   ("SNOMED", "299716001",  "| Iliac and/or femoral artery |"),
        "ILIACA":           ("SNOMED", "10293006",   "| Iliac artery |"),
        "ILIACV":           ("SNOMED", "244411005",  "| Iliac vein |"),
        "ILIUM":            ("SNOMED", "22356005",   "| Ilium |"),
        #                   ("SNOMED", "195416006",  "| Inferior cardiac vein |"),
        #                   ("SNOMED", "51249003",   "| Inferior left pulmonary vein |"),
        "INFMESA":          ("SNOMED", "33795007",   "| Inferior mesenteric artery |"),
        #                   ("SNOMED", "113273001",  "| Inferior right pulmonary vein |"),
        "INFVENACAVA":      ("SNOMED", "64131007",   "| Inferior vena cava |"),
        "INGUINAL":         ("SNOMED", "26893007",   "| Inguinal region |"),
        "INNOMINATEA":      ("SNOMED", "12691009",   "| Innominate artery |"),
        "INNOMINATEV":      ("SNOMED", "8887007",    "| Innominate vein |"),
        "IAC":              ("SNOMED", "361078006",  "| Internal Auditory Canal |"),
        "ICA":              ("SNOMED", "86117002",   "| Internal carotid artery |"),
        "INTILIACA":        ("SNOMED", "90024005",   "| Internal iliac artery |"),
        "INTJUGULARV":      ("SNOMED", "12123001",   "| Internal jugular vein |"),
        "INTMAMMARYA":      ("SNOMED", "69327007",   "| Internal mammary artery |"),
        #                   ("SNOMED", "818987002",  "| Intra-abdominopelvic |"),
        #                   ("SNOMED", "131183008",  "| Intra-articular |"),
        "INTRACRANIAL":     ("SNOMED", "1101003",    "| Intracranial |"),
        #                   ("SNOMED", "32849002",   "| Intra-esophageal |"),
        #                   ("SNOMED", "816989007",  "| Intra-pelvic |"),
        #                   ("SNOMED", "43799004",   "| Intra-thoracic |"),
        "JAW":              ("SNOMED", "661005",     "| Jaw region |"),
        "JEJUNUM":          ("SNOMED", "21306003",   "| Jejunum |"),
        "JOINT":            ("SNOMED", "39352004",   "| Joint |"),
        #                   ("SNOMED", "128563000",  "| Juxtaposed atrial appendage |"),
        "KIDNEY":           ("SNOMED", "64033007",   "| Kidney |"),
        "KNEE":             ("SNOMED", "72696002",   "| Knee |"),
        "LACRIMALA":        ("SNOMED", "59749000",   "| Lacrimal artery |"),
        #                   ("SNOMED", "128979005",  "| Lacrimal artery of right eye |"),
        "LARGEINTESTINE":   ("SNOMED", "14742008",   "| Large intestine |"),
        "LARYNX":           ("SNOMED", "4596009",    "| Larynx |"),
        "LATVENTRICLE":     ("SNOMED", "66720007",   "| Lateral Ventricle |"),
        "LATRIUM":          ("SNOMED", "82471001",   "| Left atrium |"),
        #                   ("SNOMED", "33626005",   "| Left auricular appendage |"),
        "LFEMORALA":        ("SNOMED", "113270003",  "| Left femoral artery |"),
        "LHEPATICV":        ("SNOMED", "273202007",  "| Left hepatic vein |"),
        "LHYPOCHONDRIAC":   ("SNOMED", "133945003",  "| Left hypochondriac region |"),
        "LINGUINAL":        ("SNOMED", "85119005",   "| Left inguinal region |"),
        "LLQ":              ("SNOMED", "68505006",   "| Left lower quadrant of abdomen |"),
        "LLUMBAR":          ("SNOMED", "1017210004", "| Left lumbar region |"),
        "LPORTALV":         ("SNOMED", "70253006",   "| Left portal vein |"),
        "LPULMONARYA":      ("SNOMED", "50408007",   "| Left pulmonary artery |"),
        "LUQ":              ("SNOMED", "86367003",   "| Left upper quadrant of abdomen |"),
        "LVENTRICLE":       ("SNOMED", "87878005",   "| Left ventricle |"),
        #                   ("SNOMED", "70238003",   "| Left ventricle inflow tract |"),
        #                   ("SNOMED", "13418002",   "| Left ventricle outflow tract |"),
        "LINGUALA":         ("SNOMED", "113264009",  "| Lingual artery |"),
        "LIVER":            ("SNOMED", "10200004",   "| Liver |"),
        #                   ("SNOMED", "19100000",   "| Lower inner quadrant of breast |"),
        "LOWERLEG":         ("SNOMED", "30021000",   "| Lower leg |"),
        "LOWERLIMB":        ("SNOMED", "61685007",   "| Lower limb |"),
        #                   ("SNOMED", "33564002",   "| Lower outer quadrant of breast |"),
        "LUMBARA":          ("SNOMED", "34635009",   "| Lumbar artery |"),
        "LUMBAR":           ("SNOMED", "52612000",   "| Lumbar region |"),
        "LSPINE":           ("SNOMED", "122496007",  "| Lumbar spine |"),
        "LSSPINE":          ("SNOMED", "1217253001", "| Lumbo-sacral spine |"),
        "LUMEN":            ("SNOMED", "91747007",   "| Lumen of blood vessel |"),
        "LUNG":             ("SNOMED", "39607008",   "| Lung |"),
        "MANDIBLE":         ("SNOMED", "91609006",   "| Mandible |"),
        "MASTOID":          ("SNOMED", "59066005",   "| Mastoid bone |"),
        "MAXILLA":          ("SNOMED", "70925003",   "| Maxilla |"),
        "MEDIASTINUM":      ("SNOMED", "72410000",   "| Mediastinum |"),
        "MESENTRICA":       ("SNOMED", "86570000",   "| Mesenteric artery |"),
        "MESENTRICV":       ("SNOMED", "128583004",  "| Mesenteric vein |"),
        "MCA":              ("SNOMED", "17232002",   "| Middle cerebral artery |"),
        "MIDHEPATICV":      ("SNOMED", "273099000",  "| Middle hepatic vein |"),
        "MORISONSPOUCH":    ("SNOMED", "243977002",  "| Morisons pouch |"),
        "MOUTH":            ("SNOMED", "123851003",  "| Mouth |"),
        #                   ("SNOMED", "102292000",  "| Muscle of lower limb |"),
        #                   ("SNOMED", "30608006",   "| Muscle of upper limb |"),
        #                   ("SNOMED", "74386004",   "| Nasal bone |"),
        "NASOPHARYNX":      ("SNOMED", "360955006",  "| Nasopharynx |"),
        "NECK":             ("SNOMED", "45048000",   "| Neck |"),
        "NECKCHESTABDPELV": ("SNOMED", "416319003",  "| Neck, Chest, Abdomen and Pelvis |"),
        "NECKCHESTABDOMEN": ("SNOMED", "416152001",  "| Neck, Chest and Abdomen |"),
        "NECKCHEST":        ("SNOMED", "417437006",  "| Neck and Chest |"),
        "NOSE":             ("SNOMED", "45206002",   "| Nose |"),
        "OCCPITALA":        ("SNOMED", "31145008",   "| Occipital artery |"),
        "OCCIPTALV":        ("SNOMED", "32114007",   "| Occipital vein |"),
        #                   ("SNOMED", "113346000",  "| Omental bursa |"),
        #                   ("SNOMED", "27398004",   "| Omentum |"),
        "OPHTHALMICA":      ("SNOMED", "53549008",   "| Ophthalmic artery |"),
        "OPTICCANAL":       ("SNOMED", "55024004",   "| Optic canal |"),
        "ORBIT":            ("SNOMED", "363654007",  "| Orbital structure |"),
        "OVARY":            ("SNOMED", "15497006",   "| Ovary |"),
        "PANCREAS":         ("SNOMED", "15776009",   "| Pancreas |"),
        "PANCREATICDUCT":   ("SNOMED", "69930009",   "| Pancreatic duct |"),
        "PANCBILEDUCT":     ("SNOMED", "110621006",  "| Pancreatic duct and bile duct systems |"),
        #                   ("SNOMED", "2095001",    "| Paranasal sinus |"),
        "PARASTERNAL":      ("SNOMED", "91691001",   "| Parasternal |"),
        "PARATHYROID":      ("SNOMED", "111002",     "| Parathyroid |"),
        "PAROTID":          ("SNOMED", "45289007",   "| Parotid gland |"),
        "PATELLA":          ("SNOMED", "64234005",   "| Patella |"),
        #                   ("SNOMED", "83330001",   "| Patent ductus arteriosus |"),
        "PELVIS":           ("SNOMED", "816092008",  "| Pelvis |"),
        "PELVISLOWEXTREMT": ("SNOMED", "1231522001", "| Pelvis and lower extremities |"),
        "PENILEA":          ("SNOMED", "282044005",  "| Penile artery |"),
        "PENIS":            ("SNOMED", "18911002",   "| Penis |"),
        "PERINEUM":         ("SNOMED", "38864007",   "| Perineum |"),
        "PERONEALA":        ("SNOMED", "8821006",    "| Peroneal artery |"),
        "PHANTOM":          ("SNOMED", "706342009",  "| Phantom |"),
        "PHARYNX":          ("SNOMED", "54066008",   "| Pharynx |"),
        "PHARYNXLARYNX":    ("SNOMED", "312535008",  "| Pharynx and larynx |"),
        "PLACENTA":         ("SNOMED", "78067005",   "| Placenta |"),
        "POPLITEALA":       ("SNOMED", "43899006",   "| Popliteal artery |"),
        "POPLITEALFOSSA":   ("SNOMED", "32361000",   "| Popliteal fossa |"),
        "POPLITEALV":       ("SNOMED", "56849005",   "| Popliteal vein |"),
        "PORTALV":          ("SNOMED", "32764006",   "| Portal vein |"),
        "PCA":              ("SNOMED", "70382005",   "| Posterior cerebral artery |"),
        "POSCOMMA":         ("SNOMED", "43119007",   "| Posterior communicating artery |"),
        #                   ("SNOMED", "128569001",  "| Posterior medial tributary |"),
        "POSTIBIALA":       ("SNOMED", "13363002",   "| Posterior tibial artery |"),
        #                   ("SNOMED", "14944004",   "| Primitive aorta |"),
        #                   ("SNOMED", "91707000",   "| Primitive pulmonary artery |"),
        "PROFFEMA":         ("SNOMED", "31677005",   "| Profunda femoris artery |"),
        "PROFFEMV":         ("SNOMED", "23438002",   "| Profunda femoris vein |"),
        "PROSTATE":         ("SNOMED", "41216001",   "| Prostate |"),
        "PULMONARYA":       ("SNOMED", "81040000",   "| Pulmonary artery |"),
        #                   ("SNOMED", "128584005",  "| Pulmonary artery conduit |"),
        #                   ("SNOMED", "128586007",  "| Pulmonary chamber of cor triatriatum |"),
        "PULMONARYV":       ("SNOMED", "122972007",  "| Pulmonary vein |"),
        #                   ("SNOMED", "128566008",  "| Pulmonary vein confluence |"),
        #                   ("SNOMED", "128567004",  "| Pulmonary venous atrium |"),
        "RADIALA":          ("SNOMED", "45631007",   "| Radial artery |"),
        "RADIUS":           ("SNOMED", "62413002",   "| Radius |"),
        "RADIUSULNA":       ("SNOMED", "110535000",  "| Radius and ulna |"),
        "CULDESAC":         ("SNOMED", "53843000",   "| Rectouterine pouch |"),
        "RECTUM":           ("SNOMED", "34402009",   "| Rectum |"),
        "RENALA":           ("SNOMED", "2841007",    "| Renal artery |"),
        #                   ("SNOMED", "25990002",   "| Renal pelvis |"),
        "RENALV":           ("SNOMED", "56400007",   "| Renal vein |"),
        "RETROPERITONEUM":  ("SNOMED", "82849001",   "| Retroperitoneum |"),
        "RIB":              ("SNOMED", "113197003",  "| Rib |"),
        "RATRIUM":          ("SNOMED", "73829009",   "| Right atrium |"),
        #                   ("SNOMED", "68300000",   "| Right auricular appendage |"),
        "RFEMORALA":        ("SNOMED", "69833005",   "| Right femoral artery |"),
        "RHEPATICV":        ("SNOMED", "272998002",  "| Right hepatic vein |"),
        "RHYPOCHONDRIAC":   ("SNOMED", "133946002",  "| Right hypochondriac region |"),
        "RINGUINAL":        ("SNOMED", "37117007",   "| Right inguinal region |"),
        "RLQ":              ("SNOMED", "48544008",   "| Right lower quadrant of abdomen |"),
        "RLUMBAR":          ("SNOMED", "1017211000", "| Right lumbar region |"),
        "RPORTALV":         ("SNOMED", "73931004",   "| Right portal vein |"),
        "RPULMONARYA":      ("SNOMED", "78480002",   "| Right pulmonary artery |"),
        "RUQ":              ("SNOMED", "50519007",   "| Right upper quadrant of abdomen |"),
        "RVENTRICLE":       ("SNOMED", "53085002",   "| Right ventricle |"),
        #                   ("SNOMED", "8017000",    "| Right ventricle inflow |"),
        #                   ("SNOMED", "44627009",   "| Right ventricle outflow tract |"),
        "SIJOINT":          ("SNOMED", "39723000",   "| Sacroiliac joint |"),
        "SSPINE":           ("SNOMED", "54735007",   "| Sacrum |"),
        "SFJ":              ("SNOMED", "128587003",  "| Saphenofemoral junction |"),
        "SAPHENOUSV":       ("SNOMED", "362072009",  "| Saphenous vein |"),
        "SCALP":            ("SNOMED", "41695006",   "| Scalp |"),
        "SCAPULA":          ("SNOMED", "79601000",   "| Scapula |"),
        "SCLERA":           ("SNOMED", "18619003",   "| Sclera |"),
        "SCROTUM":          ("SNOMED", "20233005",   "| Scrotum |"),
        "SELLA":            ("SNOMED", "42575006",   "| Sella turcica |"),
        "SEMVESICLE":       ("SNOMED", "64739004",   "| Seminal vesicle |"),
        "SESAMOID":         ("SNOMED", "58742003",   "| Sesamoid bones of foot |"),
        "SHOULDER":         ("SNOMED", "16982005",   "| Shoulder |"),
        "SIGMOID":          ("SNOMED", "60184004",   "| Sigmoid colon |"),
        "SKULL":            ("SNOMED", "89546000",   "| Skull |"),
        "SMALLINTESTINE":   ("SNOMED", "30315005",   "| Small intestine |"),
        "SPINALCORD":       ("SNOMED", "2748008",    "| Spinal cord |"),
        "SPINE":            ("SNOMED", "421060004",  "| Spine |"),
        "SPLEEN":           ("SNOMED", "78961009",   "| Spleen |"),
        "SPLENICA":         ("SNOMED", "22083002",   "| Splenic artery |"),
        "SPLENICV":         ("SNOMED", "35819009",   "| Splenic vein |"),
        "SCJOINT":          ("SNOMED", "7844006",    "| Sternoclavicular joint |"),
        "STERNUM":          ("SNOMED", "56873002",   "| Sternum |"),
        "STOMACH":          ("SNOMED", "69695003",   "| Stomach |"),
        "SUBCLAVIANA":      ("SNOMED", "36765005",   "| Subclavian artery |"),
        "SUBCLAVIANV":      ("SNOMED", "9454009",    "| Subclavian vein |"),
        "SUBCOSTAL":        ("SNOMED", "19695001",   "| Subcostal |"),
        #                   ("SNOMED", "5713008",    "| Submandibular area |"),
        "SUBMANDIBULAR":    ("SNOMED", "54019009",   "| Submandibular gland |"),
        #                   ("SNOMED", "170887008",  "| Submental |"),
        #                   ("SNOMED", "5076001",    "| Subxiphoid |"),
        "SFA":              ("SNOMED", "181349008",  "| Superficial femoral artery |"),
        "SFV":              ("SNOMED", "397364003",  "| Superficial femoral vein |"),
        #                   ("SNOMED", "15672000",   "| Superficial temporal artery |"),
        "LSUPPULMONARYV":   ("SNOMED", "43863001",   "| Superior left pulmonary vein |"),
        "SMA":              ("SNOMED", "42258001",   "| Superior mesenteric artery |"),
        "RSUPPULMONARYV":   ("SNOMED", "8629005",    "| Superior right pulmonary vein |"),
        "SUPTHYROIDA":      ("SNOMED", "72021004",   "| Superior thyroid artery |"),
        "SVC":              ("SNOMED", "48345005",   "| Superior vena cava |"),
        "SUPRACLAVICULAR":  ("SNOMED", "77621008",   "| Supraclavicular region of neck |"),
        "SUPRAPUBIC":       ("SNOMED", "11708003",   "| Suprapubic region |"),
        #                   ("SNOMED", "26493002",   "| Suprasternal notch |"),
        #                   ("SNOMED", "128589000",  "| Systemic collateral artery to lung |"),
        #                   ("SNOMED", "128568009",  "| Systemic venous atrium |"),
        #                   ("SNOMED", "27949001",   "| Tarsal joint |"),
        "TMJ":              ("SNOMED", "53620006",   "| Temporomandibular joint |"),
        "TESTIS":           ("SNOMED", "40689003",   "| Testis |"),
        "THALAMUS":         ("SNOMED", "42695009",   "| Thalamus |"),
        "THIGH":            ("SNOMED", "68367000",   "| Thigh |"),
        "3RDVENTRICLE":     ("SNOMED", "49841001",   "| Third ventricle |"),
        "THORACICAORTA":    ("SNOMED", "113262008",  "| Thoracic aorta |"),
        "TSPINE":           ("SNOMED", "122495006",  "| Thoracic spine |"),
        "TLSPINE":          ("SNOMED", "1217256009", "| Thoraco-lumbar spine |"),
        "THORAX":           ("SNOMED", "43799004",   "| Thorax |"),
        "THUMB":            ("SNOMED", "76505004",   "| Thumb |"),
        "THYMUS":           ("SNOMED", "9875009",    "| Thymus |"),
        "THYROID":          ("SNOMED", "69748006",   "| Thyroid |"),
        "TIBIA":            ("SNOMED", "12611008",   "| Tibia |"),
        "TIBIAFIBULA":      ("SNOMED", "110536004",  "| Tibia and fibula |"),
        "TOE":              ("SNOMED", "29707007",   "| Toe |"),
        "TONGUE":           ("SNOMED", "21974007",   "| Tongue |"),
        "TRACHEA":          ("SNOMED", "44567001",   "| Trachea |"),
        "TRACHEABRONCHUS":  ("SNOMED", "110726009",  "| Trachea and bronchus |"),
        "TRANSVERSECOLON":  ("SNOMED", "485005",     "| Transverse colon |"),
        #                   ("SNOMED", "61959006",   "| Truncus arteriosus communis |"),
        #                   ("SNOMED", "57850000",   "| Truncus coeliacus |"),
        "ULNA":             ("SNOMED", "23416004",   "| Ulna |"),
        "ULNARA":           ("SNOMED", "44984001",   "| Ulnar artery |"),
        "UMBILICALA":       ("SNOMED", "50536004",   "| Umbilical artery |"),
        "UMBILICAL":        ("SNOMED", "90290004",   "| Umbilical region |"),
        "UMBILICALV":       ("SNOMED", "284639000",  "| Umbilical vein |"),
        "UPPERARM":         ("SNOMED", "40983000",   "| Upper arm |"),
        #                   ("SNOMED", "77831004",   "| Upper inner quadrant of breast |"),
        "UPPERLIMB":        ("SNOMED", "53120007",   "| Upper limb |"),
        #                   ("SNOMED", "76365002",   "| Upper outer quadrant of breast |"),
        "UPRURINARYTRACT":  ("SNOMED", "431491007",  "| Upper urinary tract |"),
        "URETER":           ("SNOMED", "87953007",   "| Ureter |"),
        "URETHRA":          ("SNOMED", "13648007",   "| Urethra |"),
        "UTERUS":           ("SNOMED", "35039007",   "| Uterus |"),
        #                   ("SNOMED", "110639002",  "| Uterus and fallopian tubes |"),
        "VAGINA":           ("SNOMED", "76784001",   "| Vagina |"),
        #                   ("SNOMED", "118375008",  "| Vascular graft |"),
        "VEIN":             ("SNOMED", "29092000",   "| Vein |"),
        #                   ("SNOMED", "34340008",   "| Venous network |"),
        #                   ("SNOMED", "21814001",   "| Ventricle |"),
        "VERTEBRALA":       ("SNOMED", "85234005",   "| Vertebral artery |"),
        #                   ("SNOMED", "110517009",  "| Vertebral column and cranium |"),
        "VULVA":            ("SNOMED", "45292006",   "| Vulva |"),
        "WRIST":            ("SNOMED", "74670003",   "| Wrist joint |"),
        "ZYGOMA":           ("SNOMED", "13881006",   "| Zygoma |")
    }    

    #
    # Contrast Agents
    # 

    # Notes:
    # DICOM prefers to code contrast agents using "medicinal product" SNOMED-CT codes (SCT = SNOMED-CT).
    # SPHN prefers to code contrast agents using "substance" SNOMED-CT codes.

    # A dictionary mapping DICOM defined contrast agent trade names to a DICOM defined list of DICOM defined coded contrast agents:
    # Key: Contrast agent trade name.
    # Value: Tuple with:
    #        - the manufacturer (e.g., "Bracco")
    #        - a list of tuples with a coding scheme designator, code value, and a human-readable description (e.g., ("SCT", "12335007", "Diatrizoate"))
    # Link: https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_12.html Table CID 12. Imaging Contrast Agent
    dicom_contrast_agent_trade_name_dict: ClassVar[ReadOnly[dict[str, tuple[str, list[tuple[str, str, str]]]]]] = {
        "Angiovist":              ("Berlex",           [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "Cardiografin":           ("Bracco",           [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "Cystografin":            ("Bracco",           [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "Gastrografin":           ("Bracco",           [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "Gastrovist":             ("Berlex",           [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "Hypaque":                ("GE",               [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "MD":                     ("Mallinckrodt",     [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "Reno":                   ("Bracco",           [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "Renografin":             ("Bracco",           [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "Renovist":               ("Bracco",           [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "Sinografin":             ("Bracco",           [("SCT",     "12335007", "Diatrizoate"),                 # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
                                                        ("SCT",     "73212002",  "Iodipamide")]),               # SNOMED: 73212002 | Product containing iodipamide (medicinal product) |
        "Urovist":                ("Berlex",           [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |

        "Multihance":             ("Bracco",           [("SCT",    "792865009", "Gadobenate dimeglumine")]),    # SNOMED: 792865009 | Product containing gadobenic acid (medicinal product) |
        # Other writing variations:
        "Multi":                  ("Bracco",           [("SCT",    "792865009", "Gadobenate dimeglumine")]),    # SNOMED: 792865009 | Product containing gadobenic acid (medicinal product) |   # Alternative writing for "Multihance"
        
        "Gadavist":               ("",                 [("SCT",    "407976008", "Gadobutrol")]),                # SNOMED: 407976008 | Product containing gadobutrol (medicinal product) |       # EU (Gadovist) vs US (Gadavist) brand name

        "Omniscan":               ("GE",               [("SCT",    "354088005", "Gadodiamide")]),               # SNOMED: 354088005 | Product containing gadodiamide (medicinal product) |
        # Other writing variations:
        "Omniskan":               ("GE",               [("SCT",    "354088005", "Gadodiamide")]),               # SNOMED: 354088005 | Product containing gadodiamide (medicinal product) |      # Alternative writing for "Omniscan"

        "Vasovist":               ("Epix",             [("SCT",    "770982005", "Gadofosveset")]),              # SNOMED: 770982005 | Product containing gadofosveset (medicinal product) |
        "Ablavar":                ("",                 [("SCT",    "770982005", "Gadofosveset")]),              # SNOMED: 770982005 | Product containing gadofosveset (medicinal product) |
        "Magnevist":              ("Berlex",           [("SCT",    "109216000", "Gadopentetate dimeglumine")]), # SNOMED: 109216000 | Gadopentetate dimeglumine (substance) |
        "Clariscan":              ("GE",               [("SCT",    "712714000", "Gadoterate meglumine")]),      # SNOMED: 712714000 | Gadoterate meglumine (substance) |
        "Dotarem":                ("Guerbet",          [("SCT",    "712714000", "Gadoterate meglumine")]),      # SNOMED: 712714000 | Gadoterate meglumine (substance) |
        "ProHance":               ("Bracco",           [("SCT",    "353946009", "Gadoteridol")]),               # SNOMED: 353946009 | Product containing gadoteridol (medicinal product) |
        "Optimark":               ("Liebel-Flarsheim", [("SCT",    "409477004", "Gadoversetamide")]),           # SNOMED: 409477004 | Product containing gadoversetamide (medicinal product) |
        "Eovist":                 ("Bayer",            [("SCT",    "440223009", "Gadoxetate disodium")]),       # SNOMED: 440223009 | Gadoxetate disodium (substance) |
        "Renovue":                ("Bracco",           [("SCT",    "12801003",  "Iodamide meglumine")]),        # SNOMED: 12801003 | Iodamide meglumine (substance) |
        "Cholographin":           ("Bracco",           [("SCT",    "73212002",  "Iodipamide")]),                # SNOMED: 73212002 | Product containing iodipamide (medicinal product) |
        "Visipaque":              ("GE",               [("SCT",    "353962003", "Iodixanol")]),                 # SNOMED: 353962003 | Product containing iodixanol (medicinal product) |

        "Omnipaque":              ("GE",               [("SCT",    "109218004", "Iohexol")]),                   # SNOMED: 109218004 | Product containing iohexol (medicinal product) |
        # Other writing variations:
        "Omnipak":                ("GE",               [("SCT",    "109218004", "Iohexol")]),                   # SNOMED: 109218004 | Product containing iohexol (medicinal product) |          # Alternative writing for "Omnipaque"
        "Omnipaq":                ("GE",               [("SCT",    "109218004", "Iohexol")]),                   # SNOMED: 109218004 | Product containing iohexol (medicinal product) |          # Alternative writing for "Omnipaque"
        "Omnipaqe":               ("GE",               [("SCT",    "109218004", "Iohexol")]),                   # SNOMED: 109218004 | Product containing iohexol (medicinal product) |          # Alternative writing for "Omnipaque"

        "Isovue":                 ("Bracco",           [("SCT",    "109219007", "Iopamidol")]),                 # SNOMED: 109219007 | Product containing iopamidol (medicinal product) |
        "Telepaque":              ("GE",               [("SCT",    "76155001",  "Iopanoic acid")]),             # SNOMED: 76155001 | Product containing iopanoic acid (medicinal product) |
        "Pantopaque":             ("Alcon",            [("SCT",    "28121005",  "Iophendylate")]),              # SNOMED: 28121005 | Iophendylate (substance) |
        "Ultravist":              ("",                 [("SCT",    "353903006", "Iopromide")]),                 # SNOMED: 353903006 | Product containing iopromide (medicinal product) |
        "Imeron":                 ("",                 [("SCT",    "353903006", "Iopromide")]),                 # SNOMED: 353903006 | Product containing iopromide (medicinal product) |
        "Conray":                 ("Mallinckrodt",     [("SCT",    "353912008", "Iothalamate")]),               # SNOMED: 353912008 | Product containing iothalamate (medicinal product) |
        "Cysto-Conray":           ("Mallinckrodt",     [("SCT",    "353912008", "Iothalamate")]),               # SNOMED: 353912008 | Product containing iothalamate (medicinal product) |
        "Vascoray":               ("Mallinckrodt",     [("SCT",    "353912008", "Iothalamate")]),               # SNOMED: 353912008 | Product containing iothalamate (medicinal product) |
        "Optiray":                ("Mallinckrodt",     [("SCT",    "109222009", "Ioversol")]),                  # SNOMED: 109222009 | Product containing ioversol (medicinal product) |
        "Hexbrix":                ("Mallinckrodt",     [("SCT",    "412228003", "Ioxaglate")]),                 # SNOMED: 412228003 | Ioxaglate meglumine (substance) |
        "Imagenil":               ("",                 [("SCT",    "409484007", "Ioxilan")]),                   # SNOMED: 409484007 | Product containing ioxilan (medicinal product) |
        "Bilivist":               ("Berlex",           [("SCT",    "87445005",  "Ipodate")]),                   # SNOMED: 87445005 | Ipodate (substance) |
        "Oragrafin":              ("Bracco",           [("SCT",    "87445005",  "Ipodate")]),                   # SNOMED: 87445005 | Ipodate (substance) |
        "Teslascan":              ("GE",               [("RXNORM", "236987",    "Mangafodipir trisodium")]), 
        "Cholographin Meglumine": ("Bracco",           [("SCT",    "69783005",  "Meglumine iodipamide")]),      # SNOMED: 69783005 | Iodipamide meglumine (substance) |
        "Amipaque":               ("GE",               [("SCT",    "90733003",  "Metrizamide")]),               # SNOMED: 90733003 | Metrizamide (substance) |
        "Isopaque":               ("GE",               [("SCT",    "354094002", "Metrizoate")]),                # SNOMED: 354094002 | Product containing metrizoate (medicinal product) |
        "Dionosil":               ("GSK",              [("SCT",    "111158001", "Propyliodone")]),              # SNOMED: 111158001 | Propyliodone (substance) |
        "Salpix":                 ("Ortho",            [("SCT",    "32836007",  "Sodium acetrizoate")]),        # SNOMED: 32836007 | Sodium acetrizoate (substance) |
        "Cholographin Sodium":    ("Bracco",           [("SCT",    "925002",    "Sodium iodipamide")]),         # SNOMED: 925002 | Sodium iodipamide (substance) |

        # 
        # Others added by Edwin:
        #

        "Gadovist":               ("Bayer",            [("SCT",    "407976008", "Gadobutrol")]),                # SNOMED: 407976008 | Product containing gadobutrol (medicinal product) |       # EU (Gadovist) vs US (Gadavist) brand name

        "Readi-Cat":              ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |
        # Other writing variations:
        "ReadiCat":               ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "Readi-Cat"
        "RDICat":                 ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "Readi-Cat"
        "Readi Cat":              ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "Readi-Cat"
        "RediCat":                ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "Readi-Cat"
        "Redi-Cat":               ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "Readi-Cat"

        "Readi-Cat 2":            ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |
        "Readi-Cat 2 SMOOTHIE":   ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |
        "Baro-Cat":               ("Mallinckrodt",     [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |
        "Cheetah":                ("Mallinckrodt",     [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |

        "E-Z-Cat":                ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |
        # Other writing variations:
        "EZ-Cat":                 ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "E-Z-Cat"
        "EZCat":                  ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "E-Z-Cat"

        "E-Z-PAQUE":              ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |
        # Other writing variations:
        "EZ-PAQUE":               ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "E-Z-PAQUE"
        "EZPAQUE":                ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "E-Z-PAQUE"
        "E-Z-PAK":                ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "E-Z-PAQUE"
        "EZ-PAK":                 ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "E-Z-PAQUE"
        "EZPAK":                  ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "E-Z-PAQUE"
        "E-Z-PAQ":                ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "E-Z-PAQUE"
        "EZ-PAQ":                 ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "E-Z-PAQUE"
        "EZPAQ":                  ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "E-Z-PAQUE"
        "E-Z-PAQE":               ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "E-Z-PAQUE"
        "EZ-PAQE":                ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "E-Z-PAQUE"
        "EZPAQE":                 ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "E-Z-PAQUE"

        "Liquid POLIBAR PLUS":    ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |
        # Other writing variations:
        "POLIBAR PLUS":           ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "Liquid POLIBAR PLUS"
        "Liquid POLIBAR":         ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "Liquid POLIBAR PLUS"
        "POLIBAR":                ("Bracco",           [("SCT",    "25419009",  "Barium Sulfate")]),            # SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |    # Alternative writing for "Liquid POLIBAR PLUS"

        "Telebrix":               ("Guerbet",          [("SCT",    "712698009", "Ioxitalamate meglumine")]),    # SNOMED: 712698009 | Ioxitalamate meglumine (substance) |
        "MD-60":                  ("Mallinckrodt",     [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "MD-76":                  ("Mallinckrodt",     [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "Reno-30":                ("Bracco",           [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "Reno-60":                ("Bracco",           [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        "Reno-Dip":               ("Bracco",           [("SCT",     "12335007", "Diatrizoate")]),               # SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |

        "MD Gastroview":          ("Bracco",           [("SCT",    "47192000",  "Diatrizoate meglumine"),       # SNOMED: 47192000 | Meglumine amidotrizoate (substance) |
                                                        ("SCT",    "395875009", "Diatrizoate sodium")]),        # SNOMED: 395875009 | Sodium amidotrizoate (substance) |
        # Other writing variations:
        "Gastroview":             ("Bracco",           [("SCT",    "47192000",  "Diatrizoate meglumine"),       # SNOMED: 47192000 | Meglumine amidotrizoate (substance) |                      # Alternative writing for "MD Gastroview"
                                                        ("SCT",    "395875009", "Diatrizoate sodium")]),        # SNOMED: 395875009 | Sodium amidotrizoate (substance) |

        "Hypaque Meglumine":      ("GE",               [("SCT",    "47192000",  "Diatrizoate meglumine")]),     # SNOMED: 47192000 | Meglumine amidotrizoate (substance) |
        "Niopam":                 ("Bracco",           [("SCT",    "109219007", "Iopamidol")]),                 # SNOMED: 109219007 | Product containing iopamidol (medicinal product) |)
        "Iomeron":                ("Bracco",           [("SCT",    "356671000", "Iomeprol")])                   # SNOMED: 356671000 | Product containing iomeprol (medicinal product) |

        # Unclear shortnames:
        #"Opti":                  # Can be Optiray or Optimark
        #"Omni":                  # Can be Omniscan or Omnipaque
        #"Iso":                   # Can be Isoview or Isopaque
    }

    # A dictionary mapping DICOM defined coded contrast agents to a corresponding DICOM defined generic name.
    # Key: Tuple with the coding scheme designator and code value (e.g., ("SCT", "47192000"))
    # Value: Corresponding contrast agent name (e.g., "Diatrizoate meglumine")
    dicom_contrast_agent_code_dict: ClassVar[ReadOnly[dict[tuple[str, str], str]]] = {(item[0],item[1]):item[2] for _, innerlist in dicom_contrast_agent_trade_name_dict.values() for item in innerlist}

    # A dictionary mapping DICOM defined contrast agent generic names to a corresponding DICOM defined coded version.
    # Key: Contrast agent generic name (e.g., "Diatrizoate meglumine")
    # Value: Tuple with the coding scheme designator and code value (e.g., ("SCT", "47192000"))
    dicom_contrast_agent_generic_name_dict: ClassVar[ReadOnly[dict[str, tuple[str, str]]]] = {item[2]:(item[0],item[1]) for _, innerlist in dicom_contrast_agent_trade_name_dict.values() for item in innerlist}

    # A dictionary mapping DICOM defined contrast agent codes (mostly SNOMED-CT "medicinal product") to contrast agent active ingredient codes (SNOMED-CT "substance") for SPHN.
    # Key: Tuple with the coding scheme designator and code value (e.g., ("SCT", "12335007"))
    # Value: Tuple with the coding scheme designator, code value, and a human-readable description (e.g., ("SNOMED", "396020008", "| Amidotrizoate (substance) |"))
    dicom_contrast_agent_code_to_sphn_active_ingredient_snomed_code_dict: ClassVar[ReadOnly[dict[tuple[str, str], tuple[str, str, str]]]] = {
        ("SCT",     "12335007"): ("SNOMED", "396020008",  "| Amidotrizoate (substance) |"),                                             # "Diatrizoate",                        SNOMED: 12335007 | Product containing amidotrizoate (medicinal product) |
        ("SCT",    "792865009"): ("SNOMED", "414308003",  "| Meglumine gadobenate (substance) |"),                                      # "Gadobenate dimeglumine",             SNOMED: 792865009 | Product containing gadobenic acid (medicinal product) |
        ("SCT",    "407976008"): ("SNOMED", "418351005",  "| Gadobutrol (substance) |"),                                                # "Gadobutrol",                         SNOMED: 407976008 | Product containing gadobutrol (medicinal product) |
        ("SCT",    "354088005"): ("SNOMED", "396067007",  "| Gadodiamide (substance) |"),                                               # "Gadodiamide",                        SNOMED: 354088005 | Product containing gadodiamide (medicinal product) |
        ("SCT",    "770982005"): ("SNOMED", "420466007",  "| Gadofosveset (substance) |"),                                              # "Gadofosveset",                       SNOMED: 770982005 | Product containing gadofosveset (medicinal product) |
        ("SCT",    "109216000"): ("SNOMED", "109216000",  "| Gadopentetate dimeglumine (substance) |"),                                 # "Gadopentetate dimeglumine",          SNOMED: 109216000 | Gadopentetate dimeglumine (substance) |
        ("SCT",    "712714000"): ("SNOMED", "712714000",  "| Gadoterate meglumine (substance) |"),                                      # "Gadoterate meglumine",               SNOMED: 712714000 | Gadoterate meglumine (substance) |
        ("SCT",    "353946009"): ("SNOMED", "420600009",  "| Gadoteridol (substance) |"),                                               # "Gadoteridol",                        SNOMED: 353946009 | Product containing gadoteridol (medicinal product) |
        ("SCT",    "409477004"): ("SNOMED", "409476008",  "| Gadoversetamide (substance) |"),                                           # "Gadoversetamide",                    SNOMED: 409477004 | Product containing gadoversetamide (medicinal product) |
        ("SCT",    "440223009"): ("SNOMED", "440223009",  "| Gadoxetate disodium (substance) |"),                                       # "Gadoxetate disodium",                SNOMED: 440223009 | Gadoxetate disodium (substance) |
        ("SCT",    "12801003"):  ("SNOMED", "12801003",   "| Iodamide meglumine (substance) |"),                                        # "Iodamide meglumine",                 SNOMED: 12801003 | Iodamide meglumine (substance) |
        ("SCT",    "73212002"):  ("SNOMED", "398939009",  "| Iodipamide (substance) |"),                                                # "Iodipamide",                         SNOMED: 73212002 | Product containing iodipamide (medicinal product) |
        ("SCT",    "353962003"): ("SNOMED", "395750001",  "| Iodixanol (substance) |"),                                                 # "Iodixanol",                          SNOMED: 353962003 | Product containing iodixanol (medicinal product) |
        ("SCT",    "109218004"): ("SNOMED", "395751002",  "| Iohexol (substance) |"),                                                   # "Iohexol",                            SNOMED: 109218004 | Product containing iohexol (medicinal product) |
        ("SCT",    "109219007"): ("SNOMED", "395754005",  "| Iopamidol (substance) |"),                                                 # "Iopamidol",                          SNOMED: 109219007 | Product containing iopamidol (medicinal product) |
        ("SCT",    "76155001"):  ("SNOMED", "412227008",  "| Iopanoic acid (substance) |"),                                             # "Iopanoic acid",                      SNOMED: 76155001 | Product containing iopanoic acid (medicinal product) |
        ("SCT",    "28121005"):  ("SNOMED", "28121005",   "| Iophendylate (substance) |"),                                              # "Iophendylate",                       SNOMED: 28121005 | Iophendylate (substance) |
        ("SCT",    "353903006"): ("SNOMED", "395756007",  "| Iopromide (substance) |"),                                                 # "Iopromide",                          SNOMED: 353903006 | Product containing iopromide (medicinal product) |
        ("SCT",    "353912008"): ("SNOMED", "395981002",  "| Iothalamate (substance) |"),                                               # "Iothalamate",                        SNOMED: 353912008 | Product containing iothalamate (medicinal product) |
        ("SCT",    "109222009"): ("SNOMED", "395759000",  "| Ioversol (substance) |"),                                                  # "Ioversol",                           SNOMED: 109222009 | Product containing ioversol (medicinal product) |
        ("SCT",    "412228003"): ("SNOMED", "412228003",  "| Ioxaglate meglumine (substance) |"),                                       # "Ioxaglate",                          SNOMED: 412228003 | Ioxaglate meglumine (substance) |
        ("SCT",    "409484007"): ("SNOMED", "409485008",  "| Ioxilan (substance) |"),                                                   # "Ioxilan",                            SNOMED: 409484007 | Product containing ioxilan (medicinal product) |
        ("SCT",    "87445005"):  ("SNOMED", "87445005",   "| Ipodate (substance) |"),                                                   # "Ipodate",                            SNOMED: 87445005 | Ipodate (substance) |
        ("RXNORM", "236987"):    ("SNOMED", "410872002",  "| Mangafodipir trisodium (substance) |"),                                    # "Mangafodipir trisodium",
        ("SCT",    "69783005"):  ("SNOMED", "69783005",   "| Iodipamide meglumine (substance) |"),                                      # "Meglumine iodipamide",               SNOMED: 69783005 | Iodipamide meglumine (substance) |
        ("SCT",    "90733003"):  ("SNOMED", "90733003",   "| Metrizamide (substance) |"),                                               # "Metrizamide",                        SNOMED: 90733003 | Metrizamide (substance) |
        ("SCT",    "354094002"): ("SNOMED", "395792006",  "| Metrizoate (substance) |"),                                                # "Metrizoate",                         SNOMED: 354094002 | Product containing metrizoate (medicinal product) |
        ("SCT",    "111158001"): ("SNOMED", "111158001",  "| Propyliodone (substance) |"),                                              # "Propyliodone",                       SNOMED: 111158001 | Propyliodone (substance) |
        ("SCT",    "32836007"):  ("SNOMED", "32836007",   "| Sodium acetrizoate (substance) |"),                                        # "Sodium acetrizoate",                 SNOMED: 32836007 | Sodium acetrizoate (substance) |
        ("SCT",    "925002"):    ("SNOMED", "925002",     "| Sodium iodipamide (substance) |"),                                         # "Sodium iodipamide",                  SNOMED: 925002 | Sodium iodipamide (substance) |
        ("SCT",    "15158005"):  ("SNOMED", "15158005",   "| Air (substance) |"),                                                       # "Air",                                SNOMED: 15158005 | Air (substance) |
        ("SCT",    "25419009"):  ("SNOMED", "396014007",  "| Barium sulfate (substance) |"),                                            # "Barium Sulfate",                     SNOMED: 25419009 | Product containing barium sulfate (medicinal product) |
        ("SCT",    "90745007"):  ("SNOMED", "90745007",   "| Bunamiodyl (substance) |"),                                                # "Bunamiodyl",                         SNOMED: 90745007 | Bunamiodyl (substance) |
        ("SCT",    "31811003"):  ("SNOMED", "31811003",   "| Carbon dioxide (substance) |"),                                            # "Carbon dioxide",                     SNOMED: 31811003 | Carbon dioxide (substance) |
        ("SCT",    "62442005"):  ("SNOMED", "62442005",   "| Chloriodized oil (substance) |"),                                          # "Chloriodized oil",                   SNOMED: 62442005 | Chloriodized oil (substance) |
        ("SCT",    "385420005"): ("SNOMED", "385420005",  "| Contrast media (substance) |"),                                            # "Contrast agent",                     SNOMED: 385420005 | Contrast media (substance) |
        ("SCT",    "768763008"): ("SNOMED", "58281002",   "| Gadolinium (substance) |"),                                                # "Gadolinium",                         SNOMED: 768763008 | Product containing gadolinium and/or gadolinium compound (product) |
        ("SCT",    "89595000"):  ("SNOMED", "89595000",   "| Iodized oil (substance) |"),                                               # "Iodized oil",                        SNOMED: 89595000 | Iodized oil (substance) |
        ("SCT",    "86584005"):  ("SNOMED", "86584005",   "| Iodoalphionic acid (substance) |"),                                        # "Iodoalphionic acid",                 SNOMED: 86584005 | Iodoalphionic acid (substance) |
        ("SCT",    "74554008"):  ("SNOMED", "74554008",   "| Iodophthalein (substance) |"),                                             # "Iodophthalein",                      SNOMED: 74554008 | Iodophthalein (substance) |
        ("SCT",    "40710000"):  ("SNOMED", "40710000",   "| Iodopyracet (substance) |"),                                               # "Iodopyracet",                        SNOMED: 40710000 | Iodopyracet (substance) |
        ("RADLEX", "RID11585"):  ("SNOMED", "1340006004", "| Ionic iodinated radiographic imaging contrast media (substance) |"),       # "Ionic iodinated contrast agent",     SNOMED: 1340006004 | Ionic iodinated radiographic imaging contrast media (substance) |
        ("SCT",    "23053002"):  ("SNOMED", "23053002",   "| Iophenoxic acid (substance) |"),                                           # "Iophenoxic acid",                    SNOMED: 23053002 | Iophenoxic acid (substance) |
        ("RADLEX", "RID38696"):  ("SNOMED", "1340009006", "| Non-ionic iodinated radiographic imaging contrast media (substance) |"),   # "Non-ionic iodinated contrast agent", SNOMED: 1340009006 | Non-ionic iodinated radiographic imaging contrast media (substance) |
        ("SCT",    "43538006"):  ("SNOMED", "43538006",   "| Non radiopaque medium (substance) |"),                                     # "Non radiopaque medium",              SNOMED: 43538006 | Non radiopaque medium (substance) |
        ("SCT",    "24099007"):  ("SNOMED", "24099007",   "| Oxygen (substance) |"),                                                    # "Oxygen",                             SNOMED: 24099007 | Oxygen (substance) |
        ("SCT",    "419098001"): ("SNOMED", "419098001",  "| Radiographic imaging contrast media (substance) |"),                       # "Radiopaque medium",                  SNOMED: 419098001 | Radiographic imaging contrast media (substance) |
        ("SCT",    "83423008"):  ("SNOMED", "83423008",   "| Sodium diprotrizoate (substance) |"),                                      # "Sodium diprotrizoate",               SNOMED: 83423008 | Sodium diprotrizoate (substance) |
        ("SCT",    "38344006"):  ("SNOMED", "38344006",   "| Sodium iodomethamate (substance) |"),                                      # "Sodium iodomethamate",               SNOMED: 38344006 | Sodium iodomethamate (substance) |
        ("SCT",    "109212003"): ("SNOMED", "109212003",  "| Tyropanoate sodium (substance) |"),                                        # "Sodium tyropanoate",                 SNOMED: 109212003 | Tyropanoate sodium (substance) |
        ("SCT",    "11713004"):  ("SNOMED", "11713004",   "| Water (substance) |"),                                                     # "Water",                              SNOMED: 11713004 | Water (substance) |
        # Other substances added by Edwin:
        ("SCT",    "395875009"): ("SNOMED", "395875009",  "| Sodium amidotrizoate (substance) |"),                                      # "Diatrizoate sodium",                 SNOMED: 395875009 | Sodium amidotrizoate (substance) |
        ("SCT",    "47192000"):  ("SNOMED", "47192000",   "| Meglumine amidotrizoate (substance) |"),                                   # "Diatrizoate meglumine"),             SNOMED: 47192000 | Meglumine amidotrizoate (substance) |
        ("SCT",    "712698009"): ("SNOMED", "712698009",  "| Ioxitalamate meglumine (substance) |"),                                    # "Ioxitalamate meglumine",             SNOMED: 712698009 | Ioxitalamate meglumine (substance) |
        ("SCT",    "356671000"): ("SNOMED", "395753004",  "| Iomeprol (substance) |")                                                   # "Iomeprol",                           SNOMED: 356671000 | Product containing iomeprol (medicinal product) |
    }


    # 
    # Contrast Ingredients
    #

    # Note:
    # Here DICOM prefers to code contrast agent ingredients using "substance" SNOMED-CT codes. 
    # SPHN also prefers to code contrast agent ingredients using "substance" SNOMED-CT codes.

    # A dictionary mapping DICOM defined contrast ingredient terms to a DICOM defined coded version.
    # Key: Contrast ingredient term (e.g., "IODINE")
    # Value: Tuple with the coding scheme designator, code value, and human-readable description (e.g., ("SCT", "44588005", "Iodine"))
    # Link: https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.4.html#table_C.7-12
    # Link: https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_13.html Table CID 13. Imaging Contrast Agent Ingredient
    dicom_contrast_ingredient_term_dict: ClassVar[ReadOnly[dict[str, tuple[str, str, str]]]] = {
        "IODINE":           ("SCT", "44588005", "Iodine"),
        "GADOLINIUM":       ("SCT", "58281002", "Gadolinium"),
        "CARBON DIOXIDE":   ("SCT", "31811003", "Carbon Dioxide"),
        "BARIUM":           ("SCT", "39290007", "Barium"),
        "XENON":            ("SCT", "83598005", "Xenon"),
        "AIR":              ("SCT", "15158005", "Air"),
        "OXYGEN":           ("SCT", "24099007", "Oxygen"),
        "WATER":            ("SCT", "11713004", "Water"),
        "IRON":             ("SCT", "3829006",  "Iron")
    }

    # A dictionary mapping DICOM defined contrast ingredient names to a corresponding DICOM defined coded version. 
    # Key: Contrast ingredient name (e.g., "Gadolinium")
    # Value: Tuple with the coding scheme designator, code value (e.g., ("SCT", "58281002"))
    dicom_contrast_ingredient_name_dict: ClassVar[ReadOnly[dict[str, tuple[str, str]]]] = {item[2]:(item[0],item[1]) for item in dicom_contrast_ingredient_term_dict.values()}

    # A dictionary mapping DICOM defined contrast ingredient codes to the same contrast ingredient codes.
    # Key: Tuple with the coding scheme designator and code value (e.g. ("SCT", "44588005"))
    # Value: Tuple with the coding scheme designator, code value, and a human-readable description (e.g. ("SNOMED", "44588005", "| Iodine (substance) |"))
    # Note: Only the coding scheme designator "SCT" is converted to "SNOMED" and the human-readable description is from the SNOMED terminology.
    dicom_contrast_ingredient_code_to_sphn_active_ingredient_snomed_code_dict: ClassVar[ReadOnly[dict[tuple[str, str], tuple[str, str, str]]]] = {
        ("SCT", "44588005"):    ("SNOMED", "44588005", "| Iodine (substance) |"),           # "Iodine"
        ("SCT", "58281002"):    ("SNOMED", "58281002", "| Gadolinium (substance) |"),       # "Gadolinium"
        ("SCT", "31811003"):    ("SNOMED", "31811003", "| Carbon dioxide (substance) |"),   # "Carbon Dioxide"
        ("SCT", "39290007"):    ("SNOMED", "39290007", "| Barium (substance) |"),           # "Barium"
        ("SCT", "83598005"):    ("SNOMED", "83598005", "| Xenon (substance) |"),            # "Xenon"
        ("SCT", "15158005"):    ("SNOMED", "15158005", "| Air (substance) |"),              # "Air"    
        ("SCT", "24099007"):    ("SNOMED", "24099007", "| Oxygen (substance) |"),           # "Oxygen"
        ("SCT", "11713004"):    ("SNOMED", "11713004", "| Water (substance) |"),            # "Water"
        ("SCT", "3829006"):     ("SNOMED", "3829006",  "| Iron (substance) |")              # "Iron"
    }

    # A list of common contrast agent active ingredient concentrations in % or mg/mL
    contrast_agent_active_ingredient_concentrations_list: ClassVar[ReadOnly[list[str]]] = ["30", "60", "76", "140", "150", "160", "180", "200", "240", "250", "260", "270", "282", "292", "300", "320", "350", "360", "370", "380", "390", "400"]

    # Omnipaque (Iohexol):      Available in 140, 180, 240, 300, and 350 mg I/mL. (Omnipaque 300 and 350 are standard for routine body CTs).
    # Isovue (Iopamidol):       Formulated as 200, 250, 300, and 370 mg I/mL. (Isovue 370 is widely used for high-velocity CT angiograms).
    # Visipaque (Iodixanol):    Available in 270 and 320 mg I/mL. This is an iso-osmolar agent frequently used in patients with compromised kidney function.
    # Ultravist (Iopromide):    Supplied as 150, 240, 300, and 370 mg I/mL.
    # Optiray (Ioversol):       Packaged as 160, 240, 300, and 350 mg I/mL.

    # Dotarem (Gadoterate meglumine):        0.5  mmol/mL	Standard macrocyclic agent
    # ProHance (Gadoteridol):	             0.5  mmol/mL	Standard macrocyclic agent
    # Magnevist (Gadopentetate dimeglumine): 0.5  mmol/mL	Linear agent (mostly historical/discontinued)
    # MultiHance (Gadobenate dimeglumine):	 0.5  mmol/mL	Weak protein-binding; higher real-world signal
    # Gadavist / Gadovist (Gadobutrol):	     1.0  mmol/mL	Double-concentration formulation; allows for half the injection volume.
    # Vueway / Elucirem (Gadopiclenol):	     0.5  mmol/mL	High-relaxivity agent; allows a half-dose (0.05 mmol/kg) to provide identical clarity to a full standard dose.
    # Eovist / Primovist (Gadoxetic acid):	 0.25 mmol/mL	Half-concentration hepatobiliary-specific agent used exclusively for targeted liver mapping.

    # Readi-Cat 2 (Barium Sulfate): Formulated precisely at 2.1% w/v. It is deliberately a very low concentration so that it opacifies the bowel loops during a CT scan without causing harsh white artifacts that ruin the image.
    # E-Z-Paque (Barium Sulfate): Prepared at 96% w/v when reconstituted, used for standard upper GI radiographic tracking.
    # Liquid Polibar: Supplied as a high-density 105% w/v suspension, typically utilized for double-contrast barium enemas.

    # A list of all above mentioned contrast agent (brand) names and ingredient names:
    all_contrast_agent_and_ingredient_names_list: ClassVar[ReadOnly[list[str]]] = \
        list(dicom_contrast_agent_trade_name_dict.keys()) \
        + list(dicom_contrast_agent_generic_name_dict.keys()) \
        + list(dicom_contrast_ingredient_name_dict.keys())


    #
    # Administration routes
    #

    # A dictionary mapping DICOM defined coded administration routes to SNOMED codes for SPHN
    # Key: Tuple of DICOM coding scheme designator and code value (e.g., ("SCT", "47625008"))
    # Value: Tuple of SNOMED coding scheme designator, code value, and description (e.g., ("SNOMED", "47625008", "| Intravenous route (qualifier value) |"))
    # Link: https://dicom.nema.org/medical/dicom/current/output/chtml/part16/sect_CID_11.html Table CID 11. Administration Route
    # Note: Not all DICOM administration routes have a corresponding SNOMED code.
    # Link: https://dicom.nema.org/medical/dicom/Final/cp1495_ft3_badsnomedcodes.pdf
    # Note: Only the coding scheme designator "SCT" is converted to "SNOMED" and the human-readable description is from the SNOMED terminology.
    administration_routes_list: ClassVar[ReadOnly[dict[tuple[str, str], tuple[str, str, str]]]] = {
        ("SCT", "47625008"):    ("SNOMED", "47625008",   "| Intravenous route (qualifier value) |"),                # "Intravenous route",
        ("SCT", "58100008"):    ("SNOMED", "58100008",   "| Intra-arterial route (qualifier value) |"),             # "Intra-arterial route",
        ("SCT", "78421000"):    ("SNOMED", "78421000",   "| Intramuscular route (qualifier value) |"),              # "Intramuscular route",
        ("SCT", "34206005"):    ("SNOMED", "34206005",   "| Subcutaneous route (qualifier value) |"),               # "Subcutaneous route",
        ("SCT", "372464004"):   ("SNOMED", "372464004",  "| Intradermal route (qualifier value) |"),                # "Intracutaneous route", "Intradermal route",
        ("SCT", "38239002"):    ("SNOMED", "38239002",   "| Intraperitoneal route (qualifier value) |"),            # "Intraperitoneal route",
        ("SCT", "60213007"):    ("SNOMED", "60213007",   "| Intramedullary route (qualifier value) |"),             # "Intramedullary route",
        ("SCT", "72607000"):    ("SNOMED", "72607000",   "| Intrathecal route (qualifier value) |"),                # "Intrathecal route",
        ("SCT", "12130007"):    ("SNOMED", "12130007",   "| Intra-articular route (qualifier value) |"),            # "Intra-articular route",
        ("SCT", "6064005"):     ("SNOMED", "6064005",    "| Topical route (qualifier value) |"),                    # "Topical route",
        ("SCT", "26643006"):    ("SNOMED", "26643006",   "| Oral route (qualifier value) |"),                       # "Oral route",
        ("SCT", "37737002"):    ("SNOMED", "37737002",   "| Intraluminal route (qualifier value) |"),               # "Intraluminal route",
        ("SCT", "446406008"):   ("SNOMED", "446406008",  "| Inhalation technique (qualifier value) |"),             # "By inhalation",
        ("SCT", "37161004"):    ("SNOMED", "37161004",   "| Rectal route (qualifier value) |"),                     # "Per rectum",
        ("SCT", "16857009"):    ("SNOMED", "16857009",   "| Vaginal route (qualifier value) |"),                    # "Vaginal route",
        ("SCT", "372463005"):   ("SNOMED", "372463005",  "| Intracoronary route (qualifier value) |"),              # "Intracoronary route",
        ("SCT", "372460008"):   ("SNOMED", "372460008",  "| Intracardiac route (qualifier value) |"),               # "Intracardiac route",
        ("SCT", "420287000"):   ("SNOMED", "420287000",  "| Intraventricular route - cardiac (qualifier value) |"), # "Intraventricular route - cardiac",
        ("SCT", "46713006"):    ("SNOMED", "46713006",   "| Nasal route (qualifier value) |"),                      # "Nasal route",
        ("SCT", "447122006"):   ("SNOMED", "447122006",  "| Intratumor route (qualifier value) |"),                 # "Intratumor route",
        ("SCT", "1259221004"):  ("SNOMED", "1259221004", "| Intracorporus cavernosum route (qualifier value) |")    # "Intracorpus cavernosum route"
        #("NCIt", "C38244"):    ("SNOMED", "",           ""),                                                       # "Intraepithelial route",      # There used to be a SNOMED RT code: G-D111, but it is not in SNOMED CT, concept: 89947002
        #("NCIt", "C38306"):    ("SNOMED", "",           ""),                                                       # "Transluminal route",         # There used to be a SNOMED RT code: G-D142, but it is not in SNOMED CT, concept: 9942002
        #("NCIt", "C38213"):    ("SNOMED", "",           ""),                                                       # "Extraluminal route",         # There used to be a SNOMED RT code: G-D146, but it is not in SNOMED CT, concept: 31638007
        #("DCM", "127070"):     ("SNOMED", "",           ""),                                                       # "Retro-orbital route",        # A technique used to administer substances via the vascular sinus and plexus located directly 
                                                                                                                                                    # behind the eye in small research animals like mice and rats
    }
