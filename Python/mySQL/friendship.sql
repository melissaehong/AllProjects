select * from users
left join friendships on users.id = friendships.user_id
left join users as users2 on friendships.friend_id = users2.id;


select users2.first_name as friend_first, users2.last_name as friend_last from users
left join friendships on users.id = friendships.user_id
left join users as users2 on friendships.friend_id = users2.id;
