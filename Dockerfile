# Use a lightweight web server as the base image
FROM nginx:alpine

# Set the working directory inside the container
WORKDIR /usr/share/nginx/html

# Remove the default Nginx welcome page
RUN chown -R nginx:nginx /usr/share/nginx

# Copy the HTML, CSS, and JavaScript files into the container
COPY sign_up.html .
COPY create_user_style.css .
COPY create_user_validation.js .

# Expose port 80 to the outside world
EXPOSE 80

RUN chown -R nginx:nginx . 
RUN chmod 755 .
RUN chmod 644 sign_up.html && \
    chmod 644 create_user_style.css && \ 
    chmod 644 create_user_validation.js

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf", "-T"]

