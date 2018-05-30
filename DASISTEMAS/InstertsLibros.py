from peewee import *

db = SqliteDatabase('consultas_db.db')

#------------------------------ INSERTAR REGISTRO(S) A libros -------------------------------------#
print(CRUDPanel.insert_row('Libros',nombre_libro="Cien años de soledad",nombre_autor="Gabriel ",editorial_libro=" Harper, Jonathan Cape"))
print(CRUDPanel.insert_row('Libros'nombre_libro="El señor de los anillos",nombre_autor="J. R. R",editorial_libro="George allen & uniwin"))
print(CRUDPanel.insert_row('Libros',nombre_libro="1984",nombre_autor="George",editorial_libro="Secker and Warburg"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Un mundo feliz",nombre_autor="Aldous Huxley",editorial_libro="Edhasa"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Orgullo y prejuicio",nombre_autor="ane Austen",editorial_libro="Austral"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Crimen y castigo",nombre_autor="Fiódor Dostoyevski",editorial_libro="Gredos"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Lolita",nombre_autor="Vladimir Nabokov",editorial_libro="Olympia Press"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Ulises",nombre_autor="James Joyce",editorial_libro="Sylvia Beach"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Madame Bovary",nombre_autor="Gustave Flaubert",editorial_libro="Madame Bovary"))
print(CRUDPanel.insert_row('Libros',nombre_libro="En busca del tiempo perdido",nombre_autor="Marcel Proust",editorial_libro="Éditions Grasset"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Don Quijote de la Mancha",nombre_autor="Miguel de Cervantes",editorial_libro="Francisco de Robles"))
print(CRUDPanel.insert_row('Libros',nombre_libro="El retrato de Dorian Gray",nombre_autor=" Oscar Wilde",editorial_libro="Austral"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Ana Karenina",nombre_autor=" León Tolstói",editorial_libro="Austral"))
print(CRUDPanel.insert_row('Libros',nombre_libro="El Principito",nombre_autor="Antoine de Saint-Exupéry",editorial_libro="Océano Historias gráficas"))
print(CRUDPanel.insert_row('Libros',nombre_libro="El proceso",nombre_autor="Franz Kafka",editorial_libro="DICIONES CATEDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="El ruido y la furia",nombre_autor="William Faulkner",editorial_libro="DICIONES CATEDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Hamlet",nombre_autor="William Shakespeare",editorial_libro="DICIONES CATEDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Lo que el viento se llevó",nombre_autor="Margaret Mitchell",editorial_libro="PENGUIN RANDOM HOUSE GRUPO EDITORIAL ESPAÑA"))
print(CRUDPanel.insert_row('Libros',nombre_libro="La Odisea",nombre_autor="Homero",editorial_libro="PORRUA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Las uvas de la ira",nombre_autor="John Steinbeck",editorial_libro="EDICIONES CATEDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="El guardián entre el centeno",nombre_autor="J. D. Salinger",editorial_libro="ALIANZA EDITORIAL "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Cumbres borrascosas",nombre_autor="Emily Brontë",editorial_libro="PORRUA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="El gran Gatsby",nombre_autor="F. Scott Fitzgerald",editorial_libro="FONTAMARA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Mil soles espléndidos",nombre_autor="Khaled Hosseini",editorial_libro="OCEANO / SALAMANDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Alicia en el país de las maravillas",nombre_autor="Lewis Carroll",editorial_libro="Océano Historias gráficas"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Rebelión en la granja",nombre_autor="George Orwell",editorial_libro="EMU (EDITORES MEXICANOS UNIDOS) "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Los pilares de la tierra",nombre_autor="Ken Follett",editorial_libro="ALIANZA EDITORIAL "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Guerra y paz",nombre_autor="León Tolstói",editorial_libro="GRUPO EDITORIAL TOMO "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Memorias de una geisha",nombre_autor="Arthur Golden",editorial_libro="DEBOLSILLO "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Frankenstein",nombre_autor="Mary W. Shelley",editorial_libro="CASA EDITORIAL BOEK MEXICO "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Los viajes de Gulliver",nombre_autor="Jonathan Swift",editorial_libro=" PLUTON EDICIONES "))
print(CRUDPanel.insert_row('Libros',nombre_libro="La ladrona de libros",nombre_autor="Markus Zusak",editorial_libro="PENGUIN RANDOM HOUSE GRUPO EDITORIAL ESPAÑA"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Matar a un ruiseñor",nombre_autor="Harper Lee.",editorial_libro="HARPER COLLINS PUBLISHERS "))
print(CRUDPanel.insert_row('Libros',nombre_libro="El conde de Montecristo",nombre_autor="Alejandro Dumas",editorial_libro="PORRUA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Los juegos del hambre",nombre_autor=" Suzanne Collins",editorial_libro="OCEANO / TRAVESIA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Harry Potter y la piedra filosofal",nombre_autor="J. K. Rowling",editorial_libro="OCEANO / SALAMANDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="El señor de las moscas",nombre_autor="William Golding",editorial_libro=" ALIANZA EDITORIAL "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Moby Dick",nombre_autor=" Herman Melville",editorial_libro="EXODO "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Los miserables",nombre_autor="Victor Hugo",editorial_libro="PORRUA"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Las aventuras de Huckleberry Finn",nombre_autor=" Mark Twain",editorial_libro="EPOCA INFANTIL "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Tristam Shandy",nombre_autor="Laurence Sterne",editorial_libro="EDICIONES CATEDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Drácula",nombre_autor="Bram Stoker",editorial_libro="EDICIONES AVENTURA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="El nombre de la rosa",nombre_autor="Umberto Eco",editorial_libro=" DEBOLSILLO "))
print(CRUDPanel.insert_row('Libros',nombre_libro="El extranjero",nombre_autor="Albert Camus",editorial_libro="BOOKET "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Los hermanos Karamázov",nombre_autor="Fiódor Dostoyevski",editorial_libro=" PORRUA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="El amor en los tiempos del cólera",nombre_autor="Gabriel García Márquez",editorial_libro="DIANA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Harry Potter y las reliquias de la muerte",nombre_autor="J. K. Rowling",editorial_libro=" OCEANO / SALAMANDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="El código Da Vinci",nombre_autor="Dan Brown",editorial_libro=":SAL TERRAE"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Harry Potter y el prisionero de Azkaban",nombre_autor="J. K. Rowling",editorial_libro="OCEANO / SALAMANDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Cometas en el cielo",nombre_autor="Khaled Hosseini",editorial_libro="OCEANO / SALAMANDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Ensayo sobre la ceguera",nombre_autor="José Saramago",editorial_libro="DEBOLSILLO "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Las crónicas de Narnia",nombre_autor="C. S. Lewis",editorial_libro=" DESTINO "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Los renglones torcidos de Dios",nombre_autor="Torcuato Luca de Tena",editorial_libro="PLANETA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="En llamas",nombre_autor="Suzanne Collins",editorial_libro="RBA LIBROS "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Harry Potter y el cáliz de fuego",nombre_autor="J. K. Rowling",editorial_libro="OCEANO / SALAMANDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="La sombra del viento",nombre_autor="Carlos Ruiz Zafón",editorial_libro="BOOKET "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Viaje al fin de la noche",nombre_autor="Louis Ferdinand Céline",editorial_libro="EDHASA"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Harry Potter y el misterio del príncipe ",nombre_autor="J. K. Rowling",editorial_libro="OCEANO / SALAMANDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="El juego de Ender",nombre_autor="Orson Scott Card",editorial_libro="EDICIONES B "))
print(CRUDPanel.insert_row('Libros',nombre_libro="La Biblia",nombre_autor="n/a",editorial_libro="SUD"))
print(CRUDPanel.insert_row('Libros',nombre_libro="La montaña mágica",nombre_autor="Thomas Mann",editorial_libro="MIRLO "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Harry Potter y la Orden del Fénix",nombre_autor=" J. K. Rowling",editorial_libro="OCEANO / SALAMANDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="El psicoanalista",nombre_autor="John Katzenbach",editorial_libro="MANANTIAL "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Trampa 22",nombre_autor="Joseph Heller",editorial_libro="RBA / COLOFON "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Por quién doblan las campanas",nombre_autor="Hernest Hemingway",editorial_libro="EPOCA "))
print(CRUDPanel.insert_row('Libros',,nombre_libro="Dr. Jekyll y Mr. Hyde",nombre_autor="Robert Louis Stevenson",editorial_libro="FONTANA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="El médico",nombre_autor="Noah Gordon",editorial_libro="ROCABOLSILLO"))
print(CRUDPanel.insert_row('Libros',nombre_libro="La metamorfosis",nombre_autor="Franz Kafka",editorial_libro="PORRUA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="La telaraña de Carlota",nombre_autor="E.B. White",editorial_libro="NOGUER INFANTIL "))
print(CRUDPanel.insert_row('Libros',nombre_libro="La divina comedia",nombre_autor="Dante Alighieri",editorial_libro="PORRUA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="La señora Dalloway",nombre_autor="Virginia Woolf",editorial_libro="AKAL EDICIONES "))
print(CRUDPanel.insert_row('Libros',nombre_libro="Crepúsculo",nombre_autor="Stephenie Meyer",editorial_libro="DEBOLSILLO "))
print(CRUDPanel.insert_row('Libros',nombre_libro="En el camino",nombre_autor="Jack Kerouac",editorial_libro="Viking Press"))
print(CRUDPanel.insert_row('Libros',nombre_libro="La Iliada",nombre_autor="Homero",editorial_libro="AKAL"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Jane Eyre",nombre_autor="Charlotte Brontë",editorial_libro="Smith, Elder & Co."))
print(CRUDPanel.insert_row('Libros',nombre_libro="Diario",nombre_autor="Ana Frank",editorial_libro="Alienta"))
print(CRUDPanel.insert_row('Libros',nombre_libro="El retorno del Rey",nombre_autor="J.R.R. Tolkien",editorial_libro=" George Allen & Unwin"))
print(CRUDPanel.insert_row('Libros',nombre_libro="El perfume",nombre_autor="Patrick Süskind",editorial_libro="‎Diogenes Verlag	"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Fahrenheit 451",nombre_autor="Ray Bradbury",editorial_libro="Ballantine Books"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Crónica de una muerte anunciada",nombre_autor="Gabriel García Márquez",editorial_libro="‎La Oveja Negra"))
print(CRUDPanel.insert_row('Libros',nombre_libro="La casa de los espíritus",nombre_autor="Isabel Allende",editorial_libro="DEBOLSILLO"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Mientras agonizo",nombre_autor="William Faulkner",editorial_libro="ALIANZA"))
print(CRUDPanel.insert_row('Libros',nombre_libro="La isla del tesoro",nombre_autor="Robert Louis Stevenson",editorial_libro="Cassell"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Todo se desmorona",nombre_autor="Chinua Achebe",editorial_libro="Heinemann"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Emma",nombre_autor="Jane Austen",editorial_libro="ALIANZA"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Pasaje a la India",nombre_autor="E. M. Forster",editorial_libro="Edward Arnold"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Ficciones",nombre_autor="Jorge Luis Borges",editorial_libro="Emecé Editores"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Harry Potter y la cámara secreta",nombre_autor="J. K. Rowling",editorial_libro=" OCEANO / SALAMANDRA "))
print(CRUDPanel.insert_row('Libros',nombre_libro="A sangre fría",nombre_autor="Truman Capote",editorial_libro="Penguin Random House Grupo Editorial"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Rimas y leyendas",nombre_autor="Gustavo Adolfo Bécquer",editorial_libro="ALFAGUARA"))
print(CRUDPanel.insert_row('Libros',nombre_libro="El corazón es un cazador solitario",nombre_autor="Carson Mccullers",editorial_libro="Houghton Mifflin Harcourt"))
print(CRUDPanel.insert_row('Libros',nombre_libro="El Rey Lear",nombre_autor="William Shakespear",editorial_libro=" Austral"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Tormenta de espadas",nombre_autor="George R.R. Martin",editorial_libro="GIGAMESH"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Juego de tronos",nombre_autor="George R.R.Martin",editorial_libro="PLANETA"))
print(CRUDPanel.insert_row('Libros',nombre_libro="La catedral del mar",nombre_autor="Ildefonso Falcones",editorial_libro="GRIJALBO"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Progreso del peregrino",nombre_autor="John Bunyan",editorial_libro="Whitaker House"))
print(CRUDPanel.insert_row('Libros',nombre_libro="El corazón de las tinieblas",nombre_autor="Joseph Conrad",editorial_libro="JUVENTUD"))
print(CRUDPanel.insert_row('Libros',nombre_libro="Robinson Crusoe",nombre_autor="Daniel Defoe",editorial_libro=" W. Taylo"))
print(CRUDPanel.insert_row('Libros',nombre_libro="La isla de los amores infinitos",nombre_autor="Daína Chaviano",editorial_libro="DEBOLSILLO"))
print(CRUDPanel.insert_row('Libros',nombre_libro="David Copperfield",nombre_autor="Charles Dickens",editorial_libro="Bradbury and Evans"))
#------------------------------ INSERTAR REGISTRO(S) A autores ------------------------------------#
print(CRUDPanel.insert_row('Autores',nombre_autor='Gabriel', apellidos_autor='García Márquez'))
print(CRUDPanel.insert_row('Autores',nombre_autor="Gabriel ",apellido_autor="García Márquez"))
print(CRUDPanel.insert_row('Autores',nombre_autor="J. R. R. ",apellido_autor="Tolkien"))
print(CRUDPanel.insert_row('Autores',nombre_autor="George",apellido_autor=" Orwell"))
print(CRUDPanel.insert_row('Autores',,nombre_autor="Aldous",apellido_autor="Huxley"))
print(CRUDPanel.insert_row('Autores',nombre_autor=" Jane ",apellido_autor="Austen"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Fiódor",apellido_autor=" Dostoyevski"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Vladimir",apellido_autor="Nabokov"))
print(CRUDPanel.insert_row('Autores',nombre_autor="James",apellido_autor="Joyce"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Gustave",apellido_autor="Flaubert"))
print(CRUDPanel.insert_row('Autores',nombre_autor=" Marcel",apellido_autor="Proust"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Miguel",apellido_autor=" Cervantes"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Oscar",apellido_autor="Wilde"))
print(CRUDPanel.insert_row('Autores',nombre_autor="León",apellido_autor="Tolstói"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Antoine",apellido_autor="Saint-Exupéry"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Franz",apellido_autor="Kafka"))
print(CRUDPanel.insert_row('Autores',nombre_autor="William",apellido_autor="Faulkner"))
print(CRUDPanel.insert_row('Autores',nombre_autor="William",apellido_autor="Shakespeare"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Margaret",apellido_autor="Mitchell"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Homero",apellido_autor=""))
print(CRUDPanel.insert_row('Autores',nombre_autor=" John",apellido_autor="Steinbeck"))
print(CRUDPanel.insert_row('Autores',nombre_autor="J. D",apellido_autor="Salinger"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Emily",apellido_autor="Brontë"))
print(CRUDPanel.insert_row('Autores',nombre_autor=" F.",apellido_autor="Scott Fitzgerald."))
print(CRUDPanel.insert_row('Autores',nombre_autor="Khaled",apellido_autor="Hosseini"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Lewis",apellido_autor="Carroll"))
print(CRUDPanel.insert_row('Autores',nombre_autor="George",apellido_autor="Orwell"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Ken",apellido_autor="Follett"))
print(CRUDPanel.insert_row('Autores',nombre_autor="León",apellido_autor="Tolstói"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Arthur",apellido_autor="Golden"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Mary",apellido_autor="W. Shelley"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Jonathan",apellido_autor="Swift"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Markus",apellido_autor="Zusak"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Harper",apellido_autor="Lee"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Alejandro",apellido_autor="Dumas"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Suzanne",apellido_autor="Collins"))
print(CRUDPanel.insert_row('Autores',nombre_autor=" J. K",apellido_autor="Rowling."))
print(CRUDPanel.insert_row('Autores',nombre_autor="William",apellido_autor="Golding"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Herman",apellido_autor="Melville"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Victor ",apellido_autor="Hugo"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Mark",apellido_autor="Twain"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Laurence",apellido_autor="Sterne"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Bram",apellido_autor="Stoker"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Umberto",apellido_autor="Eco"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Albert",apellido_autor="Camus"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Fiódor",apellido_autor="Dostoyevski"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Gabriel",apellido_autor="García Márquez"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Dan",apellido_autor="Brown"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Khaled",apellido_autor="Hosseini"))
print(CRUDPanel.insert_row('Autores',nombre_autor="José",apellido_autor="Saramago"))
print(CRUDPanel.insert_row('Autores',nombre_autor="C. S",apellido_autor="Lewis"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Torcuato",apellido_autor="Luca de Tena"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Suzanne",apellido_autor="Collins"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Carlos",apellido_autor="Ruiz Zafón"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Louis",apellido_autor="Ferdinand Céline"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Orson",apellido_autor="Scott Card"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Thomas",apellido_autor="Mann"))
print(CRUDPanel.insert_row('Autores',nombre_autor="John",apellido_autor="Katzenbach"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Joseph",apellido_autor="Heller"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Hernest",apellido_autor="Hemingway"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Robert",apellido_autor="Louis Stevenson"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Noah",apellido_autor="Gordon"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Franz",apellido_autor="Kafka"))
print(CRUDPanel.insert_row('Autores',nombre_autor="E.B",apellido_autor="White"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Dante",apellido_autor="Alighieri"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Virginia",apellido_autor="Woolf"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Stephenie",apellido_autor="Meyer"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Jack",apellido_autor="Kerouac"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Charlotte",apellido_autor=" Brontë"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Ana",apellido_autor="Frank"))
print(CRUDPanel.insert_row('Autores',nombre_autor="J.R.R.",apellido_autor="Tolkien"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Patrick",apellido_autor="Süskind"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Ray",apellido_autor="Bradbury."))
print(CRUDPanel.insert_row('Autores',nombre_autor=" Gabriel",apellido_autor="García Márquez"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Isabel",apellido_autor="Allende"))
print(CRUDPanel.insert_row('Autores',nombre_autor="William",apellido_autor="Faulkner"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Robert",apellido_autor="Louis Stevenson"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Chinua",apellido_autor="Achebe"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Jane",apellido_autor="Austen"))
print(CRUDPanel.insert_row('Autores',nombre_autor="E. M",apellido_autor="Forster"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Jorge",apellido_autor="Luis Borges"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Truman",apellido_autor="Capote"))
print(CRUDPanel.insert_row('Autores',nombre_autor=" Gustavo",apellido_autor="Adolfo Bécquer"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Carson",apellido_autor="Mccullers"))
print(CRUDPanel.insert_row('Autores',nombre_autor="George",apellido_autor="R.R. Martin"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Ildefonso",apellido_autor="Falcones"))
print(CRUDPanel.insert_row('Autores',nombre_autor="John",apellido_autor="Bunyan"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Joseph",apellido_autor="Conrad"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Daniel",apellido_autor="Defoe"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Daína",apellido_autor="Chaviano"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Charles",apellido_autor="Dickens"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Hans",apellido_autor="Chrisian"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Jorge",apellido_autor="Luis"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Wolfgang",apellido_autor="Von"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Gunter",apellido_autor="Grass"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Knut",apellido_autor="Hamsun"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Lu",apellido_autor="Xun"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Edgar",apellido_autor="Allan Poe"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Jose",apellido_autor="Saramago"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Leo",apellido_autor="Tolstoy"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Elsa",apellido_autor="Morante"))
print(CRUDPanel.insert_row('Autores',nombre_autor="Aldous",apellido_autor="Huxley"))
#------------------------------- INSERTAR REGISTRO(S) A Editoriales -----------------------------------#
print(CRUDPanel.insert_row('Editoriales',editorial='Harper, Jonathan Cape', pais_editorial='Reino Unido'))
print(CRUDPanel.insert_row('Editoriales',editorial="George Allen & Unwin",pais_editrial="Reino Unido"))
print(CRUDPanel.insert_row('Editoriales',editorial="Secker and Warburg",pais_editrial="Reino Unido"))
print(CRUDPanel.insert_row('Editoriales',editorial="Edhasa",pais_editrial="Reino Unido"))
print(CRUDPanel.insert_row('Editoriales',editorial="Austral",pais_editrial="España"))
print(CRUDPanel.insert_row('Editoriales',editorial="Gredos",pais_editrial="Ruso"))
print(CRUDPanel.insert_row('Editoriales',editorial="Olympia Press",pais_editrial="Francia"))
print(CRUDPanel.insert_row('Editoriales',editorial="Sylvia Beach",pais_editrial="Paris"))
print(CRUDPanel.insert_row('Editoriales',editorial="Madame Bovary",pais_editrial="Francia"))
print(CRUDPanel.insert_row('Editoriales',editorial="Éditions Grasset",pais_editrial="Francia"))
print(CRUDPanel.insert_row('Editoriales',editorial="Francisco de Robles",pais_editrial="España"))
print(CRUDPanel.insert_row('Editoriales',editorial="Austral",pais_editrial="Irlanda"))
print(CRUDPanel.insert_row('Editoriales',editorial="Océano Historias gráficas",pais_editrial="Mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="DICIONES CATEDRA ",pais_editrial="España"))
print(CRUDPanel.insert_row('Editoriales',editorial="PENGUIN RANDOM HOUSE GRUPO EDITORIAL ESPAÑA",pais_editrial="ESPAÑA"))
print(CRUDPanel.insert_row('Editoriales',editorial="EMU (EDITORES MEXICANOS UNIDOS) ",pais_editrial="Ciudad de mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="PORRUA ",pais_editrial="ciudad de mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="EDICIONES CATEDRA ",pais_editrial="ESPAÑA"))
print(CRUDPanel.insert_row('Editoriales',editorial="ALIANZA EDITORIAL ",pais_editrial="ESPAÑA"))
print(CRUDPanel.insert_row('Editoriales',editorial="GRUPO EDITORIAL TOMO ",pais_editrial="ciudad de mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="DEBOLSILLO ",pais_editrial="Ciudad de mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="CASA EDITORIAL BOEK MEXICO ",pais_editrial="ciudad de mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="PLUTON EDICIONES ",pais_editrial="Mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="HARPER COLLINS PUBLISHERS ",pais_editrial="New York"))
print(CRUDPanel.insert_row('Editoriales',editorial="PORRUA ",pais_editrial="Mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="OCEANO / TRAVESIA ",pais_editrial="Mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="OCEANO / SALAMANDRA ",pais_editrial="ESPAÑA"))
print(CRUDPanel.insert_row('Editoriales',editorial=" ALIANZA EDITORIAL ",pais_editrial="ESPAÑA"))
print(CRUDPanel.insert_row('Editoriales',editorial="EXODO ",pais_editrial="MEXICO"))
print(CRUDPanel.insert_row('Editoriales',editorial="EPOCA INFANTIL ",pais_editrial="MEXICO"))
print(CRUDPanel.insert_row('Editoriales',editorial="FONTAMARA ",pais_editrial="MEXICO"))
print(CRUDPanel.insert_row('Editoriales',editorial="EDICIONES CATEDRA ",pais_editrial="ESPAÑA"))
print(CRUDPanel.insert_row('Editoriales',editorial=" EDICIONES AVENTURA ",pais_editrial="ESPAÑA"))
print(CRUDPanel.insert_row('Editoriales',editorial="BOOKET ",pais_editrial="MEXICO"))
print(CRUDPanel.insert_row('Editoriales',editorial="DIANA ",pais_editrial="MEXICO"))
print(CRUDPanel.insert_row('Editoriales',editorial="SAL TERRAE",pais_editrial="CHILE"))
print(CRUDPanel.insert_row('Editoriales',editorial="DESTINO ",pais_editrial="ESPAÑA"))
print(CRUDPanel.insert_row('Editoriales',editorial="PLANETA ",pais_editrial="ESPAÑA"))
print(CRUDPanel.insert_row('Editoriales',editorial=" RBA LIBROS ",pais_editrial="MEXICO"))
print(CRUDPanel.insert_row('Editoriales',editorial="EDHASA",pais_editrial="ARGENTINA"))
print(CRUDPanel.insert_row('Editoriales',editorial="SUD",pais_editrial="España"))
print(CRUDPanel.insert_row('Editoriales',editorial="EDICIONES B ",pais_editrial="ESPAÑA"))
print(CRUDPanel.insert_row('Editoriales',editorial="MIRLO ",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="MANANTIAL ",pais_editrial="Argentina"))
print(CRUDPanel.insert_row('Editoriales',editorial="RBA / COLOFON ",pais_editrial="España"))
print(CRUDPanel.insert_row('Editoriales',editorial="EPOCA ",pais_editrial="ESPAÑA"))
print(CRUDPanel.insert_row('Editoriales',editorial="ROCABOLSILLO",pais_editrial="ARGENTINA"))
print(CRUDPanel.insert_row('Editoriales',editorial="FONTANA ",pais_editrial="ARGENTINA"))
print(CRUDPanel.insert_row('Editoriales',editorial="NOGUER INFANTIL ",pais_editrial="CHILE"))
print(CRUDPanel.insert_row('Editoriales',editorial="AKAL EDICIONES ",pais_editrial="MEXICO"))
print(CRUDPanel.insert_row('Editoriales',editorial="Viking Press",pais_editrial="New York"))
print(CRUDPanel.insert_row('Editoriales',editorial="Smith, Elder & Co.",pais_editrial="Reyno unido"))
print(CRUDPanel.insert_row('Editoriales',editorial="Alienta",pais_editrial="España"))
print(CRUDPanel.insert_row('Editoriales',editorial="‎Diogenes Verlag",pais_editrial="Alemania"))
print(CRUDPanel.insert_row('Editoriales',editorial="Ballantine Books",pais_editrial="New York"))
print(CRUDPanel.insert_row('Editoriales',editorial="‎La Oveja Negra",pais_editrial="Colombia"))
print(CRUDPanel.insert_row('Editoriales',editorial="Cassell",pais_editrial="Reino unido"))
print(CRUDPanel.insert_row('Editoriales',editorial="Heinemann",pais_editrial="Estados Unidos"))
print(CRUDPanel.insert_row('Editoriales',editorial="Edward Arnold",pais_editrial="New York"))
print(CRUDPanel.insert_row('Editoriales',editorial="Emecé Editores",pais_editrial="Buenos aires"))
print(CRUDPanel.insert_row('Editoriales',editorial="Penguin Random House Grupo Editorial",pais_editrial="New York"))
print(CRUDPanel.insert_row('Editoriales',editorial="ALFAGUARA",pais_editrial="ESPAÑA"))
print(CRUDPanel.insert_row('Editoriales',editorial="Houghton Mifflin Harcourt",pais_editrial="Estados Unidos"))
print(CRUDPanel.insert_row('Editoriales',editorial="Austral",pais_editrial="Buenos Aires"))
print(CRUDPanel.insert_row('Editoriales',editorial="GIGAMESH",pais_editrial="España"))
print(CRUDPanel.insert_row('Editoriales',editorial="PLANETA",pais_editrial="Mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="GRIJALBO",pais_editrial="Mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="Whitaker House",pais_editrial="España"))
print(CRUDPanel.insert_row('Editoriales',editorial="JUVENTUD",pais_editrial="Mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial=" ‎W. Taylo",pais_editrial="Reino unido"))
print(CRUDPanel.insert_row('Editoriales',editorial="Bradbury and Evans",pais_editrial="Reino unido"))
print(CRUDPanel.insert_row('Editoriales',editorial="Almadía",pais_editrial="Mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="EDITORIAL ESFINGE",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="ESTACIÓN DE LECTURA",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="NORIEGA EDITORES",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="FONDO DE CULTURA ECONOMICA",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="EDUCAL",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="PAX MÉXICO",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="ARI/TIPS EN FICHAS",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="CEAC",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="EDITORIAL DE VECCHI",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="LECTORUM",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="MCGRAW-HILL INTERAMERICANA",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="EDICIONES FISCALES ISEF",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="BANCRY-MACCHI",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="MIGUEL ÁNGEL PORRÚA",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="SAN PABLO",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="EDICIONES SM",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="EDICIONES LAROUSSE",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="EDITORES MEXICANOS UNIDOS",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="PARCIFAL EDICIONES",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="EDICIONES URANO",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="ALFAOMEGA GRUPO EDITOR",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="CALIGRAMA EDITORES",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="SANTILLANA",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="PORRÚA",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="PRELUDIO",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="RICHMOND",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="LIBROS IMAGINAR (INFANTIL",pais_editrial="mexico"))
print(CRUDPanel.insert_row('Editoriales',editorial="UNAM",pais_editrial="mexico"))
