
SRC	= getenv.c 

NAME32	= getenv32
NAME64	= getenv64

CC = gcc

FLAG32	= -m32
FLAG64	= -m64

OBJ=	$(SRC:.c=.o)

all:	$(OBJ)
	$(CC) $(FLAG32) -o $(NAME32) $(SRC)
	$(CC) $(FLAG64) -o $(NAME64) $(SRC)

clean:
	rm -f $(OBJ)

fclean:	clean
	rm -f $(NAME)

re:	fclean all
