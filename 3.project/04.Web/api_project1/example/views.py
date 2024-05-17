from rest_framework import status, generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.generics import get_object_or_404 
from example.models import Book
from example.serializers import BookSerializer

# Create your views here.
@api_view(["GET"])
def helloAPI(request):
    return Response("hello world!")

# 클래스형 뷰로 HelloAPI 작성
class HelloAPI(APIView):
    def get(self,request, format = None):
        return Response("hello world!")
    
@api_view(["GET", "POST"]) # get/post 요청을 처리하게 만들어주는 데코레이터
def booksAPI(request):
    if request.method == "GET": # get 요청(도서 전체 정보)
        books = Book.objects.all() # book 모델로부터 전체 데이터 가져오기

        # 시리얼라이저에 전체 데이터를 집어넣기(직렬화)
        serializer = BookSerializer(books, many = True)

        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == "POST": # post 요청(도서 정보 등록)
        # post 요청으로 들어온 데이터를 시리얼라이저에 집어넣기
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid(): # 유효한 데이터라면
            # 시리얼라이저의 역직렬화를 통해 save(), 모델 시리얼라이저의 기본 create() 함수가 동작
            serializer.save()
            
            # 201 메시지를 보내며 성공
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        # 400 잘못된 요청
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"]) # GET = 조회, POST = 수정
def bookAPI(request, bid):
    book = get_object_or_404(Book, bid = bid) # bid = pk 인 데이터를 Book에서 가져오고, 없으면 404 에러
    serializer = BookSerializer(book) # 시리얼라이저에 데이터를 집어넣기(직렬화)
    return Response(serializer.data, status = status.HTTP_200_OK)

# 위와 같은 뷰를 클래스형으로 작성
class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid = bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs): #get 메소드 처리 함수(전체 목록 조회)
        return self.list(request, *args, **kwargs) # mixins.ListModelMixin과 연결
    
    def post(self, request, *args, **kwargs): # post 메소드 처리 함수(1권 등록)
        return self.create(request, *args, **kwargs) # mixins.CreateModelMixin과 연결
    
class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "bid" # 장고 기본 모델 pk가 아닌 bid를 pk로 사용하고 있기 때문에 lookup_field로 설정

    def get(self, request, *args, **kwargs): # get 메소드 처리 함수(1권 조회)
        return self.retrieve(request, *args, **kwargs) # mixins.RetrieveModelMixin 과 연결
    
    def put(self, request, *args, **kwargs): # put 메소드 처리 함수(1권 수정)
        return self.update(request, *args, **kwargs) # mixins.UpdateModelMixin과 연결
    
    def delete(self, request, *args, **kwargs): # delete 메소드 처리 함수(1권 삭제)
        return self.destroy(request, *args, **kwargs) # mixins.DestroyModelMixin 과 연결

# 전체목록 + 생성 조합을 사용해서 기능 구현
class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# 1개 조회 + 1개 수정 + 1개 삭제 조합을 사용해서 기능 구현
class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "bid"

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer