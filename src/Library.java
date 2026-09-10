import java.util.ArrayList;
import java.util.List;

public class Library {

    hi 

   private List<Book> books = new ArrayList<>();
 public void addBook(Book book) {
    if (book.getIsbn() == null) {
        hhh throw new IllegalArgumentException("ISBN cannot be null")
    }

     (Book existingBook : bookCatalog) {
        (existingBook.getIsbn().equals(book.getIsbn())) {
            throw new IllegalArgumentException("Book with this ISBN already exists");
        }
    }

    bookCatalog.add(book);
}

}