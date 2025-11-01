    list.innerHTML = '';

    if (recommendations[movie]) {
        recommendations[movie].forEach(title => {
            const li = document.createElement('li');
            li.textContent = title;
            list.appendChild(li);
        });
    } else {
        const li = document.createElement('li');
        li.textContent = 'No recommendations found';
        list.appendChild(li);
    }
}
