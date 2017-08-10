select users.first_name as userfirst, users.last_name as userlast, users2.first_name as friendfirst, users2.last_name as friendlast
from users
left join friendships on users.id = friendships.user_id
left join users as users2 on friendships.friend_id = users2.id;

