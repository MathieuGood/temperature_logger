<h3>Suppression d'une demande de contact</h3>
<p>
    Êtes-vous certain de vouloir supprimer la demande de contact suivante ?
</p>
<p>
    <?php ?>
</p>
<?php
$id = $_GET['id'];

if (!isset($id)) {
    echo '<a href="index.php?page=gestion_contacts">Retour à la liste des demandes de contact</a>';
} else {
    ?>
    <form method="POST" action="">
        <input class="button redbutton" type="button" onclick="window.location.href = 'index.php?page=liste_contacts'" value="Annuler">
        <input class="button" type="submit" name="validation" value="Confirmer la suppression">
    </form>
    <?php
    if (isset($_POST['validation'])) {
        $contacts_db = new Contacts();
        $contacts_db->delete($id);
        header("Location: index.php?page=gestion_contacts");
    }
}

?>
