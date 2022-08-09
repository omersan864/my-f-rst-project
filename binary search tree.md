Proje 3

[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

Örnek: root x'dir. root'un sağından y bulunur. Solunda z bulunur vb.


1. adım :    root olarak 7 elemanını seçiyorum  

2. adım :    5 elemanı 7 den küçük olduğu için soluna yazıyoruz 
				
				7
			          /
			       5


3. adım : 1 elemanı 7 den küçük daha sonra 5 elemanından da küçük o yüzden 5'in soluna yazıyoruz 

				7
			          /
			       5
			     /
			  1

4. adım : 8 elemanı 7 den büyük olduğu için sağına yazıyoruz 

				7
			          /    \
			       5         8
			     /
			  1

5. adım :  3 elemanı 7 den küçük 5 den de küçük fakat 1'den büyük olduğu için sağına yazıyoruz 

				7
			          /    \
			       5         8
			     /
			  1
			    \
			      3


6. adım : 6 elemanı 7 den küçük 7 nin soluna ama 5 den büyük olduğu için 5'in sağına

				7
			          /    \
			       5         8
			     /   \
			  1        6
			    \
			      3


7. adım : 0 değeri  1 den küçük olduğu için 1 değerinin sağına yazılır 

				7
			          /    \
			       5         8
			     /   \
			  1        6
			 /  \
		           0      3


8 adım : 9 değeri 8 den büyük olduğu için 8 değerinin sağına yazılır 

				7
			          /    \
			       5         8
			     /   \         \
			  1        6         9
			 /  \
		           0      3



9 adım : 4 değeri  3 elemanın sağına yazılır 

				7
			          /    \
			       5         8
			     /   \         \
			  1        6         9
			 /  \
		           0      3
                                             \
                                                4

10 . adım : 2 değeri 3 elemanından küçük olduğu için soluna yazılır 

				7
			          /    \
			       5         8
			     /   \         \
			  1        6         9
			 /  \
		           0      3
                                           /\
                                         2    4





































