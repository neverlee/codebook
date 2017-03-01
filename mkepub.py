import mkepub
import os

class CodeBook:
    def __init__(self, root):
        self.root = root
        self.lr = len(root) + 1

    def walk_tree(self, prepath, thedir, pchapter=None):
        mypath = os.path.join(prepath, thedir)
        print(">>", mypath[self.lr:])
        parts = os.listdir(mypath)
        for nn in parts:
            fpath = os.path.join(mypath, nn)
            if os.path.isfile(fpath):

                with open(fpath) as f:
                    data = f.read()
                    data = "<pre>\n" + data + "\n</pre>"
                    self.book.add_page(nn, data, parent=pchapter)
                print("-", fpath[self.lr:])

        for nn in parts:
            fpath = os.path.join(mypath, nn)
            if os.path.isdir(fpath):

                chapter = self.book.add_page(nn, fpath, parent=pchapter)

                self.walk_tree(mypath, nn, chapter)


    def start(self, title, author, cover=None, style=None):
        self.book = mkepub.Book(title=title, author=author)
        if cover:
            with open(cover, 'rb') as f:
                self.book.set_cover(f.read())
        if style:
            with open(style) as f:
                self.book.set_stylesheet(f.read())

        self.walk_tree("", self.root, None)

    def save(self, fpath):
        self.book.save(fpath)

cb = CodeBook("pub")
cb.start("mkepub", "listarme")
cb.save("one.epub")


#book.add_page('Chapter 3: Images', '<img src="images/chapter3.png" alt="You can use images as well">')
#with open('chapter3.png', 'rb') as file:
#    book.add_image('chapter3.png', file.read())
