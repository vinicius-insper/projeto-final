mesa1={}
mesa1['cadeira1']={'produto':[1,2,'produto',0]}
mesa1['cadeira2']={'produto':[1,2,'produto',0]}
mesa1['cadeira3']={'produto':[1,2,'produto',0]}
mesa1['cadeira4']={'produto':[1,2,'produto',0]}

mesa2={}
mesa2['cadeira1']={'produto':[1,2,'produto',0]}
mesa2['cadeira2']={'produto':[1,2,'produto',0]}
mesa2['cadeira3']={'produto':[1,2,'produto',0]}
mesa2['cadeira4']={'produto':[1,2,'produto',0]}

mesa3={} 
mesa3['cadeira1']={'produto':[1,2,'produto',0]}
mesa3['cadeira2']={'produto':[1,2,'produto',0]}
mesa3['cadeira3']={'produto':[1,2,'produto',0]}
mesa3['cadeira4']={'produto':[1,2,'produto',0]}

mesa4={}
mesa4['cadeira1']={'produto':[1,2,'produto',0]}
mesa4['cadeira2']={'produto':[1,2,'produto',0]}
mesa4['cadeira3']={'produto':[1,2,'produto',0]}
mesa4['cadeira4']={'produto':[1,2,'produto',0]}

mesa5={}
mesa5['cadeira1']={'produto':[1,2,'produto',0]}
mesa5['cadeira2']={'produto':[1,2,'produto',0]}
mesa5['cadeira3']={'produto':[1,2,'produto',0]}
mesa5['cadeira4']={'produto':[1,2,'produto',0]}

mesa6={}
mesa6['cadeira1']={'produto':[1,2,'produto',0]}
mesa6['cadeira2']={'produto':[1,2,'produto',0]}
mesa6['cadeira3']={'produto':[1,2,'produto',0]}
mesa6['cadeira4']={'produto':[1,2,'produto',0]}

mesa7={}
mesa7['cadeira1']={'produto':[1,2,'produto',0]}
mesa7['cadeira2']={'produto':[1,2,'produto',0]}
mesa7['cadeira3']={'produto':[1,2,'produto',0]}
mesa7['cadeira4']={'produto':[1,2,'produto',0]}
mesa7['cadeira5']={'produto':[1,2,'produto',0]}
mesa7['cadeira6']={'produto':[1,2,'produto',0]}

mesa8={}
mesa8['cadeira1']={'produto':[1,2,'produto',0]}
mesa8['cadeira2']={'produto':[1,2,'produto',0]}
mesa8['cadeira3']={'produto':[1,2,'produto',0]}
mesa8['cadeira4']={'produto':[1,2,'produto',0]}
mesa8['cadeira5']={'produto':[1,2,'produto',0]}
mesa8['cadeira6']={'produto':[1,2,'produto',0]}

mesa9={}
mesa9['cadeira1']={'produto':[1,2,'produto',0]}
mesa9['cadeira2']={'produto':[1,2,'produto',0]}
mesa9['cadeira3']={'produto':[1,2,'produto',0]}
mesa9['cadeira4']={'produto':[1,2,'produto',0]}
mesa9['cadeira5']={'produto':[1,2,'produto',0]}
mesa9['cadeira6']={'produto':[1,2,'produto',0]}


from firebase import firebase

firebase = firebase.FirebaseApplication("https://smartserver.firebaseio.com")
result1 = firebase.put('/',name='mesa1',data=mesa1)
result2 = firebase.put('/',name='mesa2',data=mesa2)
result3 = firebase.put('/',name='mesa3',data=mesa3)
result4 = firebase.put('/',name='mesa4',data=mesa4)
result5 = firebase.put('/',name='mesa5',data=mesa5)
result6 = firebase.put('/',name='mesa6',data=mesa6)
result7 = firebase.put('/',name='mesa7',data=mesa7)
result8 = firebase.put('/',name='mesa8',data=mesa8)
result9 = firebase.put('/',name='mesa9',data=mesa9) 
