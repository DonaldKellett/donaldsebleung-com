package website;

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
		// TODO: send the email
		sessionStatus.setComplete();
		return "redirect:/";
	}
}