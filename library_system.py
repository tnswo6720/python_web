from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 초기 멤버와 책 데이터 설정
members = {}
books = {}

@app.route('/')
def admin():
    return render_template('admin.html', members=members, books=books)

@app.route('/admin', methods=['POST'])
def admin_actions():
    if request.method == 'POST':
        if 'new_member_name' in request.form and 'new_member_phone' in request.form:
            new_member_name = request.form['new_member_name']
            new_member_phone = request.form['new_member_phone']

            if new_member_name not in members:
                members[new_member_name] = {'phone': new_member_phone, 'borrowed_books': []}

        if 'member_name_to_remove' in request.form:
            member_name_to_remove = request.form['member_name_to_remove']

            if member_name_to_remove in members:
                del members[member_name_to_remove]

        if 'new_book_title' in request.form:
            new_book_title = request.form['new_book_title']

            if new_book_title not in books:
                books[new_book_title] = '대출 가능'

        if 'book_title_to_remove' in request.form:
            book_title_to_remove = request.form['book_title_to_remove']

            if book_title_to_remove in books:
                del books[book_title_to_remove]

        if 'member_name' in request.form and 'book_title' in request.form:
            member_name = request.form['member_name']
            book_title = request.form['book_title']

            if member_name not in members:
                return "도서관 멤버가 아닙니다. 올바른 멤버 이름을 입력하세요."

            if book_title not in books:
                return "책이 존재하지 않습니다. 올바른 책 이름을 입력하세요."

            # 대출
            if 'borrow' in request.form:
                if len(members[member_name]['borrowed_books']) < 5:
                    if books[book_title] == '대출 가능':
                        members[member_name]['borrowed_books'].append(book_title)
                        books[book_title] = '대출 중'

            # 반납
            elif 'return' in request.form:
                if book_title in members[member_name]['borrowed_books']:
                    members[member_name]['borrowed_books'].remove(book_title)
                    books[book_title] = '대출 가능'

    return render_template('admin.html', members=members, books=books)

if __name__ == '__main__':
    app.run()
