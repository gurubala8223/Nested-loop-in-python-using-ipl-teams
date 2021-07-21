Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> iplteams=["MI","CSK","RC","RR","SRH","KK","DC","PK"]
>>> for same_team in iplteams:
	for different_team in iplteams:
		if same_team ==different_team:
			print(same_team +"vs" +different_team)

			
MIvsMI
CSKvsCSK
RCvsRC
RRvsRR
SRHvsSRH
KKvsKK
DCvsDC
PKvsPK
>>> iplteams=["MI","CSK","RC","RR","SRH","KK","DC","PK"]
>>> for same_team in iplteams:
	for different_team in iplteams:
		if same_team !=different_team:
			print(same_team +" vs " +different_team)

			
MI vs CSK
MI vs RC
MI vs RR
MI vs SRH
MI vs KK
MI vs DC
MI vs PK
CSK vs MI
CSK vs RC
CSK vs RR
CSK vs SRH
CSK vs KK
CSK vs DC
CSK vs PK
RC vs MI
RC vs CSK
RC vs RR
RC vs SRH
RC vs KK
RC vs DC
RC vs PK
RR vs MI
RR vs CSK
RR vs RC
RR vs SRH
RR vs KK
RR vs DC
RR vs PK
SRH vs MI
SRH vs CSK
SRH vs RC
SRH vs RR
SRH vs KK
SRH vs DC
SRH vs PK
KK vs MI
KK vs CSK
KK vs RC
KK vs RR
KK vs SRH
KK vs DC
KK vs PK
DC vs MI
DC vs CSK
DC vs RC
DC vs RR
DC vs SRH
DC vs KK
DC vs PK
PK vs MI
PK vs CSK
PK vs RC
PK vs RR
PK vs SRH
PK vs KK
PK vs DC
>>> 