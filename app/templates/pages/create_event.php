<h3>Création d'un événement</h3>

<?php

if (isset($_SESSION['open']) && $_SESSION['open'] > 0) {
    ?>

    <form class="userform" method="POST" action="">
        <table class="formtable"><p>
            <tr>
                <td>Date</td>
                <td><input type="date" name="date_evenement" value=""></td>
            </tr>
            <tr>
                <td>Heure</td>
                <td><input type="time" name="heure_evenement" value=""></td>
            </tr>
            <tr>
                <td>Tarif</td>
                <td><input type="text" name="tarif_evenement" value=""></td>
            </tr>
            <tr>
                <td>Style</td>
                <td><input type="text" name="style_evenement" value=""></td>
            </tr>
            <tr>
                <td>Artiste</td>
                <td><input type="text" name="artiste_evenement" value=""></td>
            </tr>
            <tr>
                <td>Description</td>
                <td><textarea name="texte_evenement"></textarea></td>
            </tr>
        </table></p>
            <input class="button redbutton" type="button" onclick="window.location.href = 'index.php?page=gestion_evenements'" value="Annuler">
            <input class="button" type="submit" name="validation" value="Créer l'événement">
    </form>

    <?php
    if (isset($_POST['validation'])) {
        $form_fields = ['date_evenement', 'heure_evenement', 'tarif_evenement', 'style_evenement', 'artiste_evenement', 'texte_evenement'];
        $form_values = array();

        foreach ($form_fields as $field) {
            array_push($form_values, trim($_POST[$field]));
        }
        
        $events_db = new Events();
        $events_db->createEvent($form_fields, $form_values); 

        header("Location: index.php?page=gestion_evenements");
    }

} else {
    header("Location: index.php?page=gestion_evenements");
}
?>


