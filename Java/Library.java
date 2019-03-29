/*  a simple Library tool to help analyze completed books in a small, personal library
*/

import java.util.HashMap;

public class Library{
  
  public Library(){
    
  }
  
  public void getFinishedBooks(HashMap<String, Boolean> library){
    if(library.size() <1){
        System.out.println("It's empty!");
    }else{
      System.out.println("Here are the books you finished: ");
      for(String book : library.keySet()){
        if(library.get(book)){
          System.out.println(book);
        }
        
      }
      
    }
  
  }
  
  public void getUnfinishedBooks(HashMap<String, Boolean> library){
    if(library.size() <1){
        System.out.println("It's empty!");
    }else{
      System.out.println("Here are the books you didn't finish: ");
      for(String book : library.keySet()){
        if(!library.get(book)){
          System.out.println(book);
        }
        
      }
      
    }
  
  }
  
  public static void main(String[] args){
    HashMap<String, Boolean> myBooks = new HashMap<String, Boolean>();
    myBooks.put("Road Down The Funnel", true);
    myBooks.put("Rat: A Biology", false );
    myBooks.put("TimeIn", true);
    myBooks.put("3D Food Printing", false);
    Library myLibrary = new Library();
    myLibrary.getFinishedBooks(myBooks);
    myLibrary.getUnfinishedBooks(myBooks);
    
  }
}