from Alumnos import Alumno
from PP import PP1
import os 


restricciones=[]
alumnos=[]
Ncurso=""
Nalumnos=0
reporte=""
reporte2=""
reporte3=""
def Abrir():
    global restricciones
    global alumnos
    global Ncurso
    global Nalumnos
    archivo=open("1.lfp",'r')
    cadena=archivo.read()
    archivo.close()
    cadena=cadena.strip()
    s1=cadena.split("=")
    Ncurso=s1[0]
    s2=s1[1].split("}")
    condiciones=s2[1].replace(" ","")
    restricciones2=condiciones.split(",")  #variable qu contienen los parametros 
    restricciones=restricciones2
    c1=s2[0] # cuerpo del contenido
    c1=c1.replace("{","")
    c1=c1.replace("<","")
    c1=c1.replace(">","")
    c1=c1.replace('"',"")
    c2=c1.replace("\n","")
    c3=c2.split(",")
    for i in c3:
        a0=i.split(";")
        alumnos.append(Alumno(a0[0].strip(),int(a0[1].strip())))
    Nalumnos=len(alumnos)

#for i in alumnos:
 #   print("Nombre:   " + str(i.getNombre()) + "     Nota:  " + str(i.getNota()))
notaMaxima=["",0]
notaMinima=["",0]

def Imprimir():

    global reporte
    reporte=reporte + PP1.titulotabla1  + "LISTA ESTUDIANTES" +PP1.titultabla2
    tabla=''' <table class="w3-table w3-striped w3-bordered w3-border">
            <thead class="w3-green">
        '''
    reporte=reporte+tabla
    tati='''  <tr>
            <th  scope="col"> NOMBRE</th>
            <th  scope="col"> NOTA</th>
            </tr>'''
    ##tati es la variable para titutlo (NOMBRE , NOTA)
    reporte=reporte+tati

    for i in alumnos:
        sc1='<tr> <th  scope="col"> '

        sc2=''' </th>
            <th  class="blue">'''

        sc22=''' </th>
            <th  class="red">'''
        sc3="</th> </tr>"
        if int(i.getNota())>60:
            reporte=reporte+sc1+str(i.getNombre())+sc2+str(i.getNota())+sc3
        else:
            reporte=reporte+sc1+str(i.getNombre())+sc22+str(i.getNota())+sc3


    reporte=reporte +" </thead> </table> <br> </section>"





def Ordenar_Ac(boton):
    global notaMaxima
    no=[]
    nu=[]
    for i in alumnos:
        no.append(i.getNombre())
        nu.append(int(i.getNota()))

    for top in range(len(nu)-1,0,-1):
        for i in range(top):
            if nu[i]>nu[i+1]:
                aux = nu[i]
                aux2=no[i]

                nu[i] = nu[i+1]
                no[i] = no[i+1]
                
                nu[i+1] = aux
                no[i+1] = aux2
  
    notaMaxima[0]=str(no[(len(alumnos)-1)] )
    notaMaxima[1]=str(nu[(len(alumnos)-1)] )

    notaMinima[0]=str(no[0] )
    notaMinima[1]=str(nu[0] )

    if boton==1:
        global reporte
        reporte=reporte + PP1.titulotabla1  + "NOTA ORDENADA ASCENDENTEMENTE" +PP1.titultabla2
        print("\n\t\t NOTA ORDENADA ASCENDENTEMENTE")
        tabla=''' <table class="w3-table w3-striped w3-bordered w3-border">
            <thead class="w3-green">
        '''
        reporte=reporte+tabla
        tati='''  <tr>
            <th  scope="col"> NOMBRE</th>
            <th  scope="col"> NOTA</th>
            </tr>'''
        ##tati es la variable para titutlo (NOMBRE , NOTA)
        reporte=reporte+tati

        for i in range(len(no)):
            print("Nombre :  " + no[i]+ "   Nota: " + str(nu[i]))
            sc1='<tr> <th  scope="col"> '
            sc2=''' </th>
            <th  class="blue">'''

            sc22=''' </th>
                <th  class="red">'''
            sc3="</th> </tr>"
            if int(nu[i])>60:
                reporte=reporte+sc1+str(no[i])+sc2+str(nu[i])+sc3
            else:
                reporte=reporte+sc1+str(no[i])+sc22+str(nu[i])+sc3
            
        reporte=reporte +" </thead> </table> <br> </section>"


def Ordenar_DC():
    no=[]
    nu=[]
    for i in alumnos:
        no.append(i.getNombre())
        nu.append(int(i.getNota()))

    for top in range(len(nu)-1,0,-1):
        for i in range(top):
            if nu[i]<nu[i+1]:
                aux = nu[i]
                aux2=no[i]

                nu[i] = nu[i+1]
                no[i] = no[i+1]
                
                nu[i+1] = aux
                no[i+1] = aux2
    
    print("\n\t\t NOTA ORDENADA DESCENDENTEMENTE")
    global reporte
    reporte=reporte + PP1.titulotabla1  + "NOTA ORDENADA DESCENDENTEMENTE" +PP1.titultabla2
    tabla=''' <table class="w3-table w3-striped w3-bordered w3-border">
            <thead class="w3-green">
        '''
    reporte=reporte+tabla
    tati='''  <tr>
            <th  scope="col"> NOMBRE</th>
            <th  scope="col"> NOTA</th>
            </tr>'''
    ##tati es la variable para titutlo (NOMBRE , NOTA)
    reporte=reporte+tati

    for i in range(len(no)):
        print("Nombre :  " + no[i]+ "   Nota: " + str(nu[i]))
        sc1='<tr> <th  scope="col"> '
        sc2=''' </th>
            <th  class="blue">'''

        sc22=''' </th>
            <th  class="red">'''

        sc3="</th> </tr>"

        if int(nu[i])>60:
            reporte=reporte+sc1+str(no[i])+sc2+str(nu[i])+sc3
        else:
            reporte=reporte+sc1+str(no[i])+sc22+str(nu[i])+sc3

    reporte=reporte +" </thead> </table> <br> </section>"
    


def Promedio():
    global reporte
    t=len(alumnos)
    n=0
    for i in alumnos:
        n=n+int(i.getNota())
    promedio=n/t
    promedio=round(promedio, 2)
    print("\nEl PROMEDIO ES :  " + str(promedio))
    reporte=reporte+ PP1.titulop1  +  "PROMEDIO :  " + str(promedio)+PP1.titulop2

def NMaxima():
    global reporte
    Ordenar_Ac(0)
    print("\n\t\t NOTA MAXIMA ")
    print("Nombre : " + notaMaxima[0]+ "    Nota:  " + str(notaMaxima[1]))
    reporte=reporte+ PP1.titulotabla1  +  " NOTA MAXIMA" +PP1.titultabla2

    tablam1='''<table class="w3-table w3-striped w3-bordered w3-border">
            <thead class="w3-green">
            <tr> 
    '''
    tablam2='''</tr>
            </thead>
           </table>
           <br>
           </section>
    '''
    if int(notaMaxima[1])>60:
        reporte=reporte + tablam1+ ' <th  scope="col">  '+notaMaxima[0]+'</th>  <th  class="blue">'+str(notaMaxima[1])+tablam2
    else:
        reporte=reporte + tablam1+ '<th  scope="col">'+notaMaxima[0]+'</th>  <th  class="red">'+str(notaMaxima[1])+tablam2

       
    

def NMinima():
    global reporte
    Ordenar_Ac(0)
    print("\n\t\t NOTA MINIMA ")
    print("Nombre : " + notaMinima[0]+ "    Nota:  " + str(notaMinima[1]))
    reporte=reporte+ PP1.titulotabla1  +  " NOTA MINIMA " +PP1.titultabla2

    tablam1='''<table class="w3-table w3-striped w3-bordered w3-border">
            <thead class="w3-green">
            <tr> 
    '''
    tablam2='''</tr>
            </thead>
           </table>
           <br>
           </section>
    '''
    if int(notaMinima[1])>60:
        reporte=reporte + tablam1+ '<th  scope="col">'+notaMinima[0]+'</th> <th class="blue" >'+str(notaMinima[1])+tablam2
    else:
        reporte=reporte + tablam1+ '<th  scope="col">'+notaMinima[0]+'</th> <th  class="red" >'+str(notaMinima[1])+tablam2

def Aprobados():
    global reporte
    numero=0
    for i in alumnos:
        if int(i.getNota())>60:
            numero=numero+1
    
    print("\nESTUDIANTES APROBADOS :   " + str(numero))
    reporte=reporte+ PP1.titulop1  +  " ESTUDIANTES APROBADOS :  " + str(numero)+PP1.titulop2

def Reprobados():
    global reporte
    numero=0
    for i in alumnos:
        if int(i.getNota())<61:
            numero=numero+1
    
    print("\nESTUDIANTES REPROBADOS :   " + str(numero))
    reporte=reporte+ PP1.titulop1  +  " ESTUDIANTES REPROBADOS :  " + str(numero)+PP1.titulop2



op=0

while op!=4:
    print("1)..........................Cargar Archivo")
    print("2)..........................Mostrar Reporte en Consola")
    print("3)..........................Exportar Reporte")
    print("4)..........................Salir")
    op=int(input())
    if op==1:
        Abrir()
        print("Archivo cargado con exito \n")
    elif op==2:
        print("Nombre De curso : " + Ncurso + "Estudiantes :  " + str(Nalumnos)+ "\n")
        Imprimir()
        for i in restricciones:
            if i=="ASC":
                Ordenar_Ac(1)
            elif i=="DESC":
                Ordenar_DC()
            elif i=="AVG":
                Promedio()
            elif i=="MIN":
                NMinima()
            elif i=="MAX":
                NMaxima()
            elif i=="APR":
                Aprobados()
            elif i=="REP":
                Reprobados()
    elif op==3:
        pagina=open("inicio.html","w")
        pagina.write(PP1.primera+ "   "+Ncurso+ ' </h2> <h2 class="masthead-heading text-uppercase mb-0">  ESTUDIANTES:  ' +  str(Nalumnos) +PP1.primeraCT+reporte+PP1.segunda)
        pagina.close()
        try:
            os.startfile("inicio.html")
        except Exception:
            print ("no se encontro")







