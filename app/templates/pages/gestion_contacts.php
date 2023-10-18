<h3>Suivi des demandes de contact</h3>

<?php
if (isset($_SESSION['open']) && $_SESSION['open'] > 0) {
    $contacts_db = new Contacts();
    $count_messages = $contacts_db->countMessages();
    echo "Nombre de messages dans la base : ".$count_messages.'<br><br>';
?>

<table class="table-with-borders">
    <tr>
        <th></th>
        <th>Date</th>
        <th>E-mail</th>
        <th>Nom</th>
        <th>Message</th>
    </tr>
    <tr>
    <?php

    $contacts_list = $contacts_db->getFullInfo();  

    foreach ($contacts_list as $contact) {
        echo "<td><a href='index.php?page=delete_contact&id=".$contact['id_contact']."'>❌</a></td>";
        $date = strtotime($contact['timestamp_contact']);
        echo "<td>".date("d/m/Y G:i", $date)."</td>";
        echo "<td>".$contact['email_contact']."</td>";
        echo "<td>".$contact['nom_contact']."</td>";
        echo "<td>".$contact['message_contact']."</td>";
        echo "</tr>";
    }

} else {
    header("Location: index.php?page=accueil");
}
?>
</table>