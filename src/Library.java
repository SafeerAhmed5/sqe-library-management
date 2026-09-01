import java.util.ArrayList;
import java.util.List;

public class Library {

    private List<Book> books = new ArrayList<>();

    public void addBook(Book book) {
    public void addBook(Book book) {
    for (Book existingBook : books) {
        if (existingBook.getIsbn().equals(book.getIsbn())) {
            throw new IllegalArgumentException("Book with this ISBN already exists");
        }
    }

    books.add(book);
}

}