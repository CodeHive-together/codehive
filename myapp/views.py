from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.utils.html import escape

nextId=4
topics=[
    {'id':1, 'title':'10-1', 'subtitle': '강의 리뷰', 
'body':'실험4000 실험 함수란 특정한 작업을 수행하기 위해서 필요한 명령어들을 묶어놓은 것이다. 함수가 호출되면 함수에서 정의된 명령문을 실행한 후, 다시 원래 실행하던 코드로...'},
    {'id':2, 'title':'10798 세로읽기', 'subtitle': '공통 문제', 
'body':'Str = [input() for _ in range(5)]<br>Len = [len(i) for i in range Str]...'},
    {'id':3, 'title':'10845 큐큐큐큐큐큐큐','subtitle': '개인 문제',
'body':'import sys<br>n = int(sys.stdin.readline())...'},
]

def search(request):
    global topics
    # 검색어 가져오기 및 공백 제거
    query = request.GET.get('query', '').strip()

    # 검색어 필터링
    filtered_topics = [
        topic for topic in topics
        if query.lower() in topic['title'].lower() or query.lower() in topic['subtitle'].lower() or query.lower() in topic['body'].lower()
    ]

    # 검색 결과가 없을 경우 메시지 출력
    if not filtered_topics:
        article = f'<h2>검색 결과가 없습니다: "{escape(query)}"</h2>'
        contextUI = ''
    else:
        article = ''
        contextUI = ''.join(f'''
            <div class="card"> 
                <div class="Title">{escape(topic["subtitle"])}</div>
                <div class="Header">{escape(topic["title"])}</div>
                <div class="Body">{escape(topic["body"])}</div>
                <div class="Buttons">
                    <a href="/update/{topic['id']}" class="btc">수정</a>
                    <a href="/read/{topic['id']}" class="btc">보기</a> 
                </div>
            </div>
        ''' for topic in filtered_topics)

    # 필터링된 결과만 전달
    return HttpResponse(HTMLTemplate(article, contextUI=contextUI, filtered_topics=filtered_topics, query=query))


def achievement(request):
    return render(request, 'myapp/achievement.html')

def index(request):
    article='''
    <h2>이 곳은 게시판 입니다.</h2>
    글 작성 및 수정, 글 읽기가 가능합니다.
    '''
    return HttpResponse(HTMLTemplate(article))

def HTMLTemplate(articleTag, id=None, contextUI='', filtered_topics=None, query=''):
    global topics

    if filtered_topics is None:
        filtered_topics = topics

    ol=''
    if filtered_topics:
        for topic in filtered_topics:
            ol+= f'''
            <div class="card"> 
                <div class="Title">{topic["subtitle"]}</div>
                <div class="Header">{topic["title"]}</div>
                <div class="Body">{topic["body"]}</div>
                <div class="Buttons">
                    <a href="/update/{topic['id']}" class="btc">수정</a>
                    <a href="/read/{topic['id']}" class="btc">보기</a> 
                </div>
            </div>
            '''
    else:
        for topic in topics:
            ol+= f'''
            <div class="card"> 
                <div class="Title">{topic["subtitle"]}</div>
                <div class="Header">{topic["title"]}</div>
                <div class="Body">{topic["body"]}</div>
                <div class="Buttons">
                    <a href="/update/{topic['id']}" class="btc">수정</a>
                    <a href="/read/{topic['id']}" class="btc">보기</a> 
                </div>
            </div>
            '''

    contextUI = ''

    return f'''
    <html>
    <head>
        <style>
            body {{
                text-align: center;  /* 중앙정렬한거 */
                background-color: #f9f9f9;
            }}
            .card {{
                background: white;
                border-radius: 10px;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                padding: 20px;
                margin: 20px auto;
                max-width: 600px; 
            }}
            .Title {{
                font-size: 18px;
                font-weight: bold;
                color: #333;
                margin-bottom: 10px;
                padding: 5px;
                background-color: #e0e0e0;
                border-radius: 5px;
            }}
            .Header {{
                font-size: 24px;
                color: #000;
                margin: 5px 0;
            }}
            .Body {{
                font-size: 16px;
                color: #666;
                margin: 10px 0;
            }}
            .Buttons {{
                margin-top: 15px;
            }}
            .mit {{
                display: inline-block;
                padding: 10px 20px; 
                font-size: 16px; 
                color: black;
                background-color: #00FF77; 
                border: 1px solid #000000;
                border-radius: 6px; 
                text-decoration: none; 
                transition: background-color 0.3s;
            }}
            .mit:hover {{
                background-color: #00AD51;
            }}
            .del {{
                display: inline-block;
                padding: 10px 20px; 
                font-size: 16px; 
                color: white;
                background-color: #FF0000; 
                border: 1px solid #000000;
                border-radius: 6px; 
                text-decoration: none; 
                transition: background-color 0.3s;
            }}
            .del:hover {{
                background-color: #761A1A;
            }}
            .btc {{
                display: inline-block;
                padding: 10px 20px; 
                font-size: 16px; 
                color: black;
                background-color: #FFFFFF; 
                border: 1px solid #000000;
                border-radius: 25px; 
                text-decoration: none; 
                transition: background-color 0.3s;
            }}
            .btc:hover {{
                background-color: #e0e0e0;
            }}
        </style>
    </head>
    <body>
    이동하기: 게시판 / <a href="/achievements/">성과 가시화</a> / 정리 업로드
    <h1><a href="/">게시판</a></h1><br>
    
    <form action="/search/" method="get">
        <input type="text" name="query" class="search" placeholder="검색어를 입력하세요" value="{escape(query)}">
        <button type="submit" class="search-button">검색</button>
    </form>
    
    <a href="/create/" class="btc"><b>글 작성</b></a>
    <ul>
        {ol}
    </ul>
    {articleTag}
    <ul>
        {contextUI}
    </ul>
    </body>
    </html>'''

def read(request, id):
    global topics
    article=''
    for topic in topics:
        if topic['id']==int(id):
            article=f'<h2>{topic["title"]}</h2><h3>{topic["subtitle"]}</h3>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def update(request, id):
    global topics
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "title": topic['title'],
                    "subtitle": topic['subtitle'],
                    "body": topic['body']
                }
        article = f'''
            <form action="/update/{id}/" method="post"><br>
            <p><input type="text" name="subtitle" value="{escape(selectedTopic["subtitle"])}"></p>
            <p><input type="text" name="title" style="width: 60%;" value="{escape(selectedTopic["title"])}"></p>
            <p><textarea name="body" style="width: 60%; height: 200px;">{escape(selectedTopic['body'])}</textarea></p>
            <p>
                    <input type="submit" class="mit" value="수정 완료">
                    <button type="submit" formaction="/delete/" name="id" value="{id}" class="del" style="margin-left: 10px;">글 삭제</button>
                </p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, id, contextUI=''))
    elif request.method == 'POST':
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['subtitle'] = subtitle
                topic['body'] = body
        return redirect(f'/read/{id}')

@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post"><br>
            <p><input type="text" name="subtitle" placeholder="글의 종류를 입력하세요"></p>
            <p><input type="text" name="title" placeholder="제목을 작성하세요" style="width: 60%;"></p>
            <p><textarea name="body" placeholder="내용을 작성하세요" style="width: 60%; height: 200px;"></textarea></p>
            <p><input type="submit" class="mit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        body = request.POST['body']
        newTopic = {"id": nextId, "title": title, "subtitle": subtitle, "body": body}
        topics.append(newTopic)
        url = '/read/' + str(nextId)
        nextId += 1
        return redirect(url)

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id=request.POST['id']
        newTopics=[]
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics=newTopics
        return redirect('/')