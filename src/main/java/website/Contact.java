package website;

import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Email;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class Contact {
	
	@NotNull(message="Name cannot be null")
	@NotEmpty(message="Name cannot be empty")
	private String name;
	
	@NotNull(message="Email cannot be null")
	@NotEmpty(message="Email cannot be empty")
	@Email(message="Email must be valid")
	private String email;
	
	@NotNull(message="Category cannot be null")
	private Category category;
	
	@NotNull(message="Message cannot be null")
	@NotEmpty(message="Message cannot be empty")
	private String message;
}