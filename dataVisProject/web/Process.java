import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
/**
 * Servlet implementation class Process
 */
@WebServlet("/Process")
public class Process extends HttpServlet {
    ...
    ...
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // TODO Auto-generated method stub
 
        String name[]=request.getParameterValues("pName");
        String age[]=request.getParameterValues("age");
        String gender[]=request.getParameterValues("gender");
 
        System.out.println(name.length);
 
        for (int i=0;i<name.length;i++)
            System.out.println(name[i]  + " " + age[i] + " " + gender[i]);
 
    }
 
}