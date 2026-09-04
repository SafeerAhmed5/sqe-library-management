import java.util.ArrayList;
import java.util.List;

public class Library {




 public void addBook(Book book) {
    if (book.getIsbn() == null) {
        throw new IllegalArgumentException("ISBN cannot be null");
    }

    for (Book existingBook : bookCatalog) {
        if (existingBook.getIsbn().equals(book.getIsbn())) {
            throw new IllegalArgumentException("Book with this ISBN already exists");
        }
    }

    bookCatalog.add(book);
}

}