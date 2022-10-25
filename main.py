import csv


class BooksWorker:
    handled_list = list()

    def read_books(self, file_name):
        with open(file_name) as csvfile:
            bookreader = csv.reader(csvfile, delimiter='|', quotechar='"')
            for row in bookreader:
                self.handled_list.append(row)

    def get_books(self, title) -> list:
        result_list = list()
        for row in self.handled_list:
            if title.lower() in row[1].lower():
                result_list.append(row)
        return result_list

    def get_totals(self, input_list, low_limit, number_to_add) -> list:
        result_list = list()
        for row in input_list:
            sum = float(row[3]) * float(row[4])
            if sum < low_limit:
                sum += number_to_add
            result_tuple = (row[1], sum)
            result_list.append(result_tuple)
        return result_list


def main():
    bw = BooksWorker()
    bw.read_books("books.csv")
    print(bw.handled_list)
    founded_books = bw.get_books("python")
    print(founded_books)
    print(bw.get_totals(founded_books, 200, 100))


main()
