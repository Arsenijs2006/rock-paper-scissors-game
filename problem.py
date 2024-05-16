// Importējam nepieciešamās bibliotēkas
const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

// Definējam Express aplikāciju
const app = express();

// Iestatām bodyParser, lai apstrādātu JSON datus
app.use(bodyParser.json());

// Ceļš uz failu, kurā glabāsies kontakti
const contactsFile = 'contacts.json';

// GET pieprasījums, lai iegūtu visus kontaktus
app.get('/contacts', (req, res) => {
    // Lasām kontaktu failu
    fs.readFile(contactsFile, 'utf8', (err, data) => {
        if (err) {
            console.error(err);
            res.status(500).send('Servera kļūda');
            return;
        }
        // Pārsūtam kontaktu datus kā atbildi
        res.json(JSON.parse(data));
    });
});

// POST pieprasījums, lai pievienotu jaunu kontaktu
app.post('/contacts', (req, res) => {
    // Iegūstam jauno kontaktu no pieprasījuma ķermeņa
    const newContact = req.body;

    // Lasām esošos kontaktus
    fs.readFile(contactsFile, 'utf8', (err, data) => {
        if (err) {
            console.error(err);
            res.status(500).send('Servera kļūda');
            return;
        }

        // Papildinām esošos kontaktus ar jauno kontaktu
        const contacts = JSON.parse(data);
        contacts.push(newContact);

        // Saglabājam jaunos kontaktus failā
        fs.writeFile(contactsFile, JSON.stringify(contacts), (err) => {
            if (err) {
                console.error(err);
                res.status(500).send('Servera kļūda');
                return;
            }
            // Atgriežam veiksmīgu atbildi
            res.status(201).send('Kontakts pievienots veiksmīgi');
        });
    });
});

// Palaižam serveri
const port = 3000;
app.listen(port, () => {
    console.log(`Serveris darbojas uz portu ${port}`);
});
