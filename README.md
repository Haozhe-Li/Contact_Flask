# Contact Flask

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FHaozhe-Li%2FContactFlask&env=MAIL_SERVER,MAIL_PASSWORD,MAIL_USERNAME,MAIL_SENDER,MAIL_FORWARD,MAIL_NAME&envDescription=All%20the%20SMTP%20mail%20requires) [<img width="50" src="https://user-images.githubusercontent.com/25181517/183423775-2276e25d-d43d-4e58-890b-edbc88e915f7.png" alt="Flask" title="Flask"/>](https://flask.palletsprojects.com/en/3.0.x/) [<img width="50" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/>](https://www.python.org)

This is a simple email server built with Flask and Flask-Mail. It works fast and seamlessly with your contact form on your static website.

## Demo

Check online demo on my website [haozheli.com](https://www.haozheli.com/#contact)

## Usage

To use this email server, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Haozhe-Li/Contact_Flask.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the environment variables:

    - `MAIL_SERVER`: SMTP server address
    - `MAIL_USERNAME`: SMTP server username.
    - `MAIL_PASSWORD`: SMTP server password. **You may need to generate a secret key or an application-specific password.** Don't know how? [Check FAQ](#FAQ).
    - `MAIL_SENDER`: Email address to send emails from
    - `MAIL_FORWARD`: Email address to forward emails to
    - `MAIL_NAME`: Name to display in the email

4. Run the Flask application:

    ```bash
    python3 app.py
    ```

5. Access the contact form on your static website and start receiving emails!

## Deployment

1. Click here to [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FHaozhe-Li%2FContactFlask&env=MAIL_SERVER,MAIL_PASSWORD,MAIL_USERNAME,MAIL_SENDER,MAIL_FORWARD,MAIL_NAME&envDescription=All%20the%20SMTP%20mail%20requires), or you can manually deployed to any platform if you like

2. Configure the environment variables as [mentioned above](#Usage), also configure your domain (it would be ok if you use the ``vercel.app`` )

3. Create a contact form in your static website, here is an example:

   ````html
   <form id="emailForm">
           <label for="name">Name:</label>
           <input type="text" id="name" name="name" required><br><br>
           <label for="email">Email:</label>
           <input type="email" id="email" name="email" required><br><br>
           <label for="message">Message:</label>
           <textarea id="message" name="message" required></textarea><br><br>
           <button type="submit">Send</button>
   </form>
   ````

4. Add the javascript at the buttom of your html file before ``</body>``, remember to change ``YOUR_DOMAIN`` to the one you have deployed on vercel.

   ````js
   <script>
           document.getElementById('emailForm').addEventListener('submit', function(event) {
               event.preventDefault();
   
               const name = document.getElementById('name').value;
               const email = document.getElementById('email').value;
               const message = document.getElementById('message').value;
   
               const data = {
                   name: name,
                   email: email,
                   message: message
               };
   
               fetch('YOUR_DOMAIN/send_email', {
                   method: 'POST',
                   headers: {
                       'Content-Type': 'application/json'
                   },
                   body: JSON.stringify(data)
               })
               .then(response => {
                   if (!response.ok) {
                       throw new Error(`HTTP error! status: ${response.status}`);
                   }
                   return response.json();
               })
               .then(data => {
                   console.log('Success:', data);
                   alert('Email sent successfully!');
               })
               .catch((error) => {
                   console.error('Error:', error);
                   alert('There was an error sending the email. Check the console for more details.');
               });
           });
       </script>
   ````

5. If you are still confused, check out the [``demo.html``](demo.html) file. Feel free to download it and use it on your own website. 

## FAQ

#### Q: Wrong Email Password or related problem when logging in to SMTP

**A:** The most common reason is that your email provider has enforced an **app-specific password** to protect your account. You will probably need to generate a unique password for this project. 

Common Email Provider SMTP articles here:

- [Gmail](https://www.gmass.co/blog/gmail-smtp/)
- [iCloud](https://support.apple.com/en-us/102525)
- [Outlook](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-for-outlook-com-d088b986-291d-42b8-9564-9c414e2aa040)
- [163](https://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2a5feb28b66796d3b)
- [QQ](https://service.mail.qq.com/detail/0/310)

Your email provider is not listed here? Try searching ``Your email provider`` + ``SMTP`` on Google, then you will find the solution.

#### Q: Wrong Email Username or related problem when logging in to SMTP

**A:**  This usually happens when you have multiple email addresses under the same account. Please make sure you select your **main email address** instead of the alias or forwarded address.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

