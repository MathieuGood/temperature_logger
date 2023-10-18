<h3>Modification d'un événement</h3>

<?php
$id = $_GET['id'];

if (!isset($id)) {
    header("Location: index.php?page=gestion_evenements");
} else {

    $events_db = new Events($id);
    ?>

    <form class="userform" method="POST" action="">
        <table class="formtable"><p>
            <tr>
                <td>Date</td>
                <td><input type="date" name="date_evenement" value="<?php echo $events_db->get('date_evenement') ?>"></td>
            </tr>
            <tr>
                <td>Heure</td>
                <td><input type="time" name="heure_evenement" value="<?php echo $events_db->get('heure_evenement') ?>"></td>
            </tr>
            <tr>
                <td>Tarif</td>
                <td><input type="text" name="tarif_evenement" value="<?php echo $events_db->get('tarif_evenement') ?>"></td>
            </tr>
            <tr>
                <td>Style</td>
                <td><input type="text" name="style_evenement" value="<?php echo $events_db->get('style_evenement') ?>"></td>
            </tr>
            <tr>
                <td>Artiste</td>
                <td><input type="text" name="artiste_evenement" value="<?php echo $events_db->get('artiste_evenement') ?>"></td>
            </tr>
            <tr>
                <td>Description</td>
                <td><textarea name="texte_evenement"><?php echo $events_db->get('texte_evenement') ?></textarea></td>
            </tr>
        </table></p>
            <input class="button redbutton" type="button" onclick="window.location.href = 'index.php?page=gestion_evenements'" value="Annuler">
            <input class="button" type="submit" name="validation" value="Confirmer les modifications">
    </form>


    <?php
    if (isset($_POST['validation'])) {
        $form_fields = ['date_evenement', 'heure_evenement', 'tarif_evenement', 'style_evenement', 'artiste_evenement', 'texte_evenement'];

        foreach ($form_fields as $field) {
            $events_db->updateEvent($id, $field, trim($_POST[$field]));   
        }
        header("Location: index.php?page=gestion_evenements");
    }
}
    ?>


