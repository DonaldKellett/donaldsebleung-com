package website;

import javax.servlet.RequestDispatcher;
import javax.servlet.http.HttpServletRequest;

import org.springframework.boot.web.servlet.error.ErrorController;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class MyErrorController implements ErrorController {
	
	@RequestMapping("/error")
	public String handleError(HttpServletRequest request, Model model) {
		Object status = request.getAttribute(RequestDispatcher.ERROR_STATUS_CODE);
		int statusCode = status == null ?
			HttpStatus.INTERNAL_SERVER_ERROR.value() :
			Integer.valueOf(status.toString());
		String statusMsg;
		try {
			statusMsg = HttpStatus.valueOf(statusCode).getReasonPhrase();
		} catch (Exception e) {
			statusMsg = HttpStatus.INTERNAL_SERVER_ERROR.getReasonPhrase();
		}
		String statusDesc = statusCode / 100 == 4 ?
				"Whoops, it seems you did something wrong as a 4xx status code signifies a user error." :
			statusCode / 100 == 5 ?
				"Whoops, it seems there's something wrong on our end as a 5xx status code signifies a server error." :
				"Whoops, it seems there might be something wrong on our end but we can't figure out exactly what.";
		model.addAttribute("statusCode", statusCode);
		model.addAttribute("statusMsg", statusMsg);
		model.addAttribute("statusDesc", statusDesc);
		return "error";
	}
}