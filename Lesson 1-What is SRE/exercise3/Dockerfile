# Alpine linux is favored due to its compact nature
FROM alpine:3.6

# Install nginx and create an index.html
RUN apk -U add nginx && echo "hello!" > /var/www/index.html

# Add the basic nginx config and nginx defaults to let nginx run
ADD nginx.conf /etc/nginx/nginx.conf
ADD nginx.default /etc/nginx/conf.d/default.conf

# The basis for any commands we'll run in the future
ENTRYPOINT [ "nginx" ]
