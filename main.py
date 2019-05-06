from app import app


def main():
    app.run(debug=True)
    # app.run(debug=True, use_reloader=False)


if __name__ == '__main__':
    main()
