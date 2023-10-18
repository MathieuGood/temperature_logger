<h3>Contact</h3>
<p>Des questions ? Des remarques à nous communiquer ? <br/> Utilisez le formulaire ci-dessous pour nous envoyer un message.</p>
<div class="content">
    <form class="userform" method="POST" action="">
        <table class="formtable"><p>
            <tr>
                <th colspan="2"></th>
            </tr>
                <th>Votre nom</th>
                <td><input type="text" name="date_evenement" value=""></td>
            </tr>
            <tr>
                <th>Votre email</th>
                <td><input type="text" name="heure_evenement" value=""></td>
            </tr>
            <tr>
                <th>Votre message</th>
                <td><textarea name="texte_evenement"></textarea></td>
            </tr>
        </table></p>
            <input class="button" type="submit" name="validation" value="Envoyer le message">
    </form>
</div>

<?php
if (isset($_POST['validation'])) {
    $form_fields = ['date_evenement', 'heure_evenement', 'tarif_evenement', 'style_evenement', 'artiste_evenement', 'texte_evenement'];
    $form_values = array();

    foreach ($form_fields as $field) {
        array_push($form_values, trim($_POST[$field]));
    }
    
    $events_db = new Events();
    $events_db->createEvent($form_fields, $form_values); 

    echo "Votre message a été envoyé à l'équipe de l'Espae Django";

}