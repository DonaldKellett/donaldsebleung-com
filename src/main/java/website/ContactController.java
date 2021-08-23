package website;

import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.Errors;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.SessionAttributes;
import org.springframework.web.bind.support.SessionStatus;

@Controller
@RequestMapping("/contact")
@SessionAttributes({"personal", "academic", "professional"})
public class ContactController {
	
	private String categoryToEmail(Category category) {
		switch (category) {
		case PERSONAL:
			return "donaldsebleung@gmail.com";
		case ACADEMIC:
			return "donaldseb.leung@alumni.ust.hk";
		case PROFESSIONAL:
			return "donaldleung@cre.com.hk";
		default:
			return null;
		}
	}
	
	@GetMapping
	public String showContactForm(Model model) {
		model.addAttribute("personal", Category.PERSONAL);
		model.addAttribute("academic", Category.ACADEMIC);
		model.addAttribute("professional", Category.PROFESSIONAL);
		model.addAttribute("contact", new Contact());
		return "contact";
	}
	
	@PostMapping
	public String processContactForm(@Valid Contact contact, Errors errors, SessionStatus sessionStatus) {
		if (errors.hasErrors()) {
			return "contact";
		}
		sessionStatus.setComplete();
		String mailtoUrl = "mailto:" + categoryToEmail(contact.getCategory()) +
				"?subject=" + URLEncoder.encode("Private message from " + contact.getName() +
						" <" + contact.getEmail() + ">", StandardCharsets.UTF_8) +
				"&body=" + URLEncoder.encode(contact.getMessage(), StandardCharsets.UTF_8);
		return "redirect:" + mailtoUrl;
	}
}