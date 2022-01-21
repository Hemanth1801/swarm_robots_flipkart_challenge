import pandas as pd

df=pd.read_csv("destinations.csv")
bot1 =df.loc[df['Induct Station'] == 1]
bot2=df.loc[df['Induct Station'] == 2]
bot1_destinations=bot1.loc[:,'Destination'].tolist()
bot2_destinations=bot2.loc[:,'Destination'].tolist()
Ahmedabad=[['Ahmedabad'],[[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]]
Pune=[['Pune'],[[[130, 136], [[177, 137], [168, 387], [201, 386]], [235, 386]], [[[201, 386], [168, 387], [177, 137]], [130, 136]]]]
Mumbai=[['Mumbai'],[[[144, 137], [[263, 145], [264, 106]], [264, 75]], [[[264, 106], [263, 145]], [144, 137]]]]
Delhi=[['Delhi'],[[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]]
Jaipur=[['Jaipur'],[[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]]
Kolkata=[['Kolkata'],[[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]]
Bengaluru=[['Bengaluru'],[[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]]
Chennai=[['Chennai'],[[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]]
Hyderabad=[['Hyderabad'],[[[167, 140], [[549, 154], [558, 205]], [557, 241]], [[[558, 205], [549, 154]], [167, 140]]]]
paths=[]
path=[]
for i in bot1_destinations:
    if str(i)=='Ahmedabad':
        path.append(Ahmedabad)
    if str(i)=='Hyderabad':
        path.append(Hyderabad)
    if str(i)=='Chennai':
        path.append(Chennai)
    if str(i) == 'Bengaluru':
        path.append(Bengaluru)
    if str(i) == 'Kolkata':
        path.append(Kolkata)
    if str(i) == 'Jaipur':
        path.append(Jaipur)
    if str(i) == 'Delhi':
        path.append(Delhi)
    if str(i) == 'Mumbai':
        path.append(Mumbai)
    if str(i) == 'Pune':
        path.append(Pune)

bot1paths=[[['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Kolkata'], [[[125, 320], [[487, 321], [490, 100], [511, 102]], [544, 103]], [[[511, 102], [490, 100], [487, 321]], [125, 320]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Kolkata'], [[[125, 320], [[487, 321], [490, 100], [511, 102]], [544, 103]], [[[511, 102], [490, 100], [487, 321]], [125, 320]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Kolkata'], [[[125, 320], [[487, 321], [490, 100], [511, 102]], [544, 103]], [[[511, 102], [490, 100], [487, 321]], [125, 320]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Kolkata'], [[[125, 320], [[487, 321], [490, 100], [511, 102]], [544, 103]], [[[511, 102], [490, 100], [487, 321]], [125, 320]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Kolkata'], [[[125, 320], [[487, 321], [490, 100], [511, 102]], [544, 103]], [[[511, 102], [490, 100], [487, 321]], [125, 320]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Kolkata'], [[[125, 320], [[487, 321], [490, 100], [511, 102]], [544, 103]], [[[511, 102], [490, 100], [487, 321]], [125, 320]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Kolkata'], [[[125, 320], [[487, 321], [490, 100], [511, 102]], [544, 103]], [[[511, 102], [490, 100], [487, 321]], [125, 320]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Kolkata'], [[[125, 320], [[487, 321], [490, 100], [511, 102]], [544, 103]], [[[511, 102], [490, 100], [487, 321]], [125, 320]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Kolkata'], [[[125, 320], [[487, 321], [490, 100], [511, 102]], [544, 103]], [[[511, 102], [490, 100], [487, 321]], [125, 320]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Kolkata'], [[[125, 320], [[487, 321], [490, 100], [511, 102]], [544, 103]], [[[511, 102], [490, 100], [487, 321]], [125, 320]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Jaipur'], [[[128, 319], [[543, 320], [543, 350]], [541, 379]], [[[543, 350], [543, 320]], [128, 319]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Pune'], [[[128, 319], [[236, 319], [236, 355]], [237, 386]], [[[236, 355], [236, 319]], [128, 319]]]], [['Kolkata'], [[[125, 320], [[487, 321], [490, 100], [511, 102]], [544, 103]], [[[511, 102], [490, 100], [487, 321]], [125, 320]]]], [['Hyderabad'], [[[129, 320], [[550, 320], [557, 274]], [559, 242]], [[[557, 274], [550, 320]], [129, 320]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Chennai'], [[[128, 319], [[234, 319], [243, 267]], [246, 230]], [[[243, 267], [234, 319]], [128, 319]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Bengaluru'], [[[130, 318], [[404, 323], [406, 268]], [407, 238]], [[[406, 268], [404, 323]], [130, 318]]]], [['Delhi'], [[[126, 321], [[453, 334], [444, 92]], [407, 91]], [[[444, 92], [453, 334]], [126, 321]]]], [['Mumbai'], [[[126, 318], [[325, 319], [329, 79], [301, 78]], [261, 75]], [[[301, 78], [329, 79], [325, 319]], [126, 318]]]], [['Ahmedabad'], [[[137, 319], [[402, 329], [402, 365]], [401, 399]], [[[402, 365], [402, 329]], [137, 319]]]]]
bot2paths=[[['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Pune'], [[[130, 136], [[177, 137], [168, 387], [201, 386]], [235, 386]], [[[201, 386], [168, 387], [177, 137]], [130, 136]]]], [['Mumbai'], [[[144, 137], [[263, 145], [264, 106]], [264, 75]], [[[264, 106], [263, 145]], [144, 137]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Jaipur'], [[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]], [['Mumbai'], [[[144, 137], [[263, 145], [264, 106]], [264, 75]], [[[264, 106], [263, 145]], [144, 137]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Jaipur'], [[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Hyderabad'], [[[167, 140], [[549, 154], [558, 205]], [557, 241]], [[[558, 205], [549, 154]], [167, 140]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Hyderabad'], [[[167, 140], [[549, 154], [558, 205]], [557, 241]], [[[558, 205], [549, 154]], [167, 140]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Jaipur'], [[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Jaipur'], [[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]], [['Pune'], [[[130, 136], [[177, 137], [168, 387], [201, 386]], [235, 386]], [[[201, 386], [168, 387], [177, 137]], [130, 136]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Mumbai'], [[[144, 137], [[263, 145], [264, 106]], [264, 75]], [[[264, 106], [263, 145]], [144, 137]]]], [['Jaipur'], [[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]], [['Hyderabad'], [[[167, 140], [[549, 154], [558, 205]], [557, 241]], [[[558, 205], [549, 154]], [167, 140]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Jaipur'], [[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Pune'], [[[130, 136], [[177, 137], [168, 387], [201, 386]], [235, 386]], [[[201, 386], [168, 387], [177, 137]], [130, 136]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Jaipur'], [[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]], [['Jaipur'], [[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]], [['Jaipur'], [[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Mumbai'], [[[144, 137], [[263, 145], [264, 106]], [264, 75]], [[[264, 106], [263, 145]], [144, 137]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Hyderabad'], [[[167, 140], [[549, 154], [558, 205]], [557, 241]], [[[558, 205], [549, 154]], [167, 140]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Mumbai'], [[[144, 137], [[263, 145], [264, 106]], [264, 75]], [[[264, 106], [263, 145]], [144, 137]]]], [['Hyderabad'], [[[167, 140], [[549, 154], [558, 205]], [557, 241]], [[[558, 205], [549, 154]], [167, 140]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Pune'], [[[130, 136], [[177, 137], [168, 387], [201, 386]], [235, 386]], [[[201, 386], [168, 387], [177, 137]], [130, 136]]]], [['Mumbai'], [[[144, 137], [[263, 145], [264, 106]], [264, 75]], [[[264, 106], [263, 145]], [144, 137]]]], [['Hyderabad'], [[[167, 140], [[549, 154], [558, 205]], [557, 241]], [[[558, 205], [549, 154]], [167, 140]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Pune'], [[[130, 136], [[177, 137], [168, 387], [201, 386]], [235, 386]], [[[201, 386], [168, 387], [177, 137]], [130, 136]]]], [['Hyderabad'], [[[167, 140], [[549, 154], [558, 205]], [557, 241]], [[[558, 205], [549, 154]], [167, 140]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Hyderabad'], [[[167, 140], [[549, 154], [558, 205]], [557, 241]], [[[558, 205], [549, 154]], [167, 140]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Jaipur'], [[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]], [['Hyderabad'], [[[167, 140], [[549, 154], [558, 205]], [557, 241]], [[[558, 205], [549, 154]], [167, 140]]]], [['Pune'], [[[130, 136], [[177, 137], [168, 387], [201, 386]], [235, 386]], [[[201, 386], [168, 387], [177, 137]], [130, 136]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Pune'], [[[130, 136], [[177, 137], [168, 387], [201, 386]], [235, 386]], [[[201, 386], [168, 387], [177, 137]], [130, 136]]]], [['Hyderabad'], [[[167, 140], [[549, 154], [558, 205]], [557, 241]], [[[558, 205], [549, 154]], [167, 140]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Mumbai'], [[[144, 137], [[263, 145], [264, 106]], [264, 75]], [[[264, 106], [263, 145]], [144, 137]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Pune'], [[[130, 136], [[177, 137], [168, 387], [201, 386]], [235, 386]], [[[201, 386], [168, 387], [177, 137]], [130, 136]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Jaipur'], [[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Jaipur'], [[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]], [['Pune'], [[[130, 136], [[177, 137], [168, 387], [201, 386]], [235, 386]], [[[201, 386], [168, 387], [177, 137]], [130, 136]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Mumbai'], [[[144, 137], [[263, 145], [264, 106]], [264, 75]], [[[264, 106], [263, 145]], [144, 137]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Hyderabad'], [[[167, 140], [[549, 154], [558, 205]], [557, 241]], [[[558, 205], [549, 154]], [167, 140]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Mumbai'], [[[144, 137], [[263, 145], [264, 106]], [264, 75]], [[[264, 106], [263, 145]], [144, 137]]]], [['Pune'], [[[130, 136], [[177, 137], [168, 387], [201, 386]], [235, 386]], [[[201, 386], [168, 387], [177, 137]], [130, 136]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Mumbai'], [[[144, 137], [[263, 145], [264, 106]], [264, 75]], [[[264, 106], [263, 145]], [144, 137]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Mumbai'], [[[144, 137], [[263, 145], [264, 106]], [264, 75]], [[[264, 106], [263, 145]], [144, 137]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Hyderabad'], [[[167, 140], [[549, 154], [558, 205]], [557, 241]], [[[558, 205], [549, 154]], [167, 140]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Pune'], [[[130, 136], [[177, 137], [168, 387], [201, 386]], [235, 386]], [[[201, 386], [168, 387], [177, 137]], [130, 136]]]], [['Jaipur'], [[[143, 137], [[482, 158], [475, 342], [474, 387], [509, 383]], [537, 381]], [[[509, 383], [474, 387], [475, 342], [482, 158]], [143, 137]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Mumbai'], [[[144, 137], [[263, 145], [264, 106]], [264, 75]], [[[264, 106], [263, 145]], [144, 137]]]], [['Pune'], [[[130, 136], [[177, 137], [168, 387], [201, 386]], [235, 386]], [[[201, 386], [168, 387], [177, 137]], [130, 136]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Chennai'], [[[144, 139], [[253, 140], [250, 194]], [248, 227]], [[[250, 194], [253, 140]], [144, 139]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Bengaluru'], [[[146, 137], [[406, 153], [409, 202]], [406, 236]], [[[409, 202], [406, 153]], [146, 137]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]], [['Ahmedabad'], [[[141, 135], [[325, 145], [326, 398], [366, 398]], [400, 398]], [[[366, 398], [326, 398], [325, 145]], [141, 135]]]], [['Delhi'], [[[146, 138], [[406, 150], [405, 118]], [407, 79]], [[[405, 118], [406, 150]], [146, 138]]]], [['Kolkata'], [[[133, 138], [[547, 163], [549, 125]], [552, 96]], [[[549, 125], [547, 163]], [133, 138]]]]]