# coding=utf-8


first_names_male = (
    'Adrien', 'Aimé', 'Alain', 'Alexandre', 'Alfred', 'Alphonse', 'André', 'Antoine', 'Arthur', 'Auguste',
    'Augustin', 'Benjamin', 'Benoît', 'Bernard', 'Bertrand', 'Charles', 'Christophe', 'Daniel', 'David', 'Denis',
    'Édouard', 'Émile', 'Emmanuel', 'Éric', 'Étienne', 'Eugène', 'François', 'Franck', 'Frédéric', 'Gabriel',
    'Georges', 'Gérard', 'Gilbert', 'Gilles', 'Grégoire', 'Guillaume', 'Guy', 'William', 'Henri', 'Honoré',
    'Hugues', 'Isaac', 'Jacques', 'Jean', 'Jérôme', 'Joseph', 'Jules', 'Julien', 'Laurent', 'Léon', 'Louis', 'Luc',
    'Lucas', 'Marc', 'Marcel', 'Martin', 'Matthieu', 'Maurice', 'Michel', 'Nicolas', 'Noël', 'Olivier', 'Patrick',
    'Paul', 'Philippe', 'Pierre', 'Raymond', 'Rémy', 'René', 'Richard', 'Robert', 'Roger', 'Roland', 'Sébastien',
    'Stéphane', 'Théodore', 'Théophile', 'Thibaut', 'Thibault', 'Thierry', 'Thomas', 'Timothée', 'Tristan',
    'Victor', 'Vincent', 'Xavier', 'Yves', 'Zacharie'
)

first_names_female = (
    'Adélaïde', 'Adèle', 'Adrienne', 'Agathe', 'Agnès', 'Aimée', 'Alexandrie', 'Alix', 'Alexandria', 'Alex',
    'Alice', 'Amélie', 'Anaïs', 'Anastasie', 'Andrée', 'Anne', 'Anouk', 'Antoinette', 'Arnaude', 'Astrid', 'Audrey',
    'Aurélie', 'Aurore', 'Bernadette', 'Brigitte', 'Capucine', 'Caroline', 'Catherine', 'Cécile', 'Céline',
    'Célina', 'Chantal', 'Charlotte', 'Christelle', 'Christiane', 'Christine', 'Claire', 'Claudine', 'Clémence',
    'Colette', 'Constance', 'Corinne', 'Danielle', 'Denise', 'Diane', 'Dorothée', 'Édith', 'Éléonore', 'Élisabeth',
    'Élise', 'Élodie', 'Émilie', 'Emmanuelle', 'Françoise', 'Frédérique', 'Gabrielle', 'Geneviève', 'Hélène',
    'Henriette', 'Hortense', 'Inès', 'Isabelle', 'Jacqueline', 'Jeanne', 'Jeannine', 'Joséphine', 'Josette',
    'Julie', 'Juliette', 'Laetitia', 'Laure', 'Laurence', 'Lorraine', 'Louise', 'Luce', 'Lucie', 'Lucy',
    'Madeleine', 'Manon', 'Marcelle', 'Margaux', 'Margaud', 'Margot', 'Marguerite', 'Margot', 'Margaret', 'Maggie',
    'daisy', 'Marianne', 'Marie', 'Marine', 'Marthe', 'Martine', 'Maryse', 'Mathilde', 'Michèle', 'Michelle',
    'Michelle', 'Monique', 'Nathalie', 'Nath', 'Nathalie', 'Nicole', 'Noémi', 'Océane', 'Odette', 'Olivie',
    'Patricia', 'Paulette', 'Pauline', 'Pénélope', 'Philippine', 'Renée', 'Sabine', 'Simone', 'Sophie', 'Stéphanie',
    'Susanne', 'Suzanne', 'Susan', 'Suzanne', 'Sylvie', 'Thérèse', 'Valentine', 'Valérie', 'Véronique', 'Victoire',
    'Virginie', 'Zoé',
    'Camille', 'Claude', 'Dominique'
)

first_names = first_names_male + first_names_female

last_names = (
    'Martin', 'Bernard', 'Thomas', 'Robert', 'Petit', 'Dubois', 'Richard', 'Garcia', 'Durand', 'Moreau', 'Lefebvre',
    'Simon', 'Laurent', 'Michel', 'Leroy', 'Martinez', 'David', 'Fontaine', 'Da Silva', 'Morel', 'Fournier',
    'Dupont', 'Bertrand', 'Lambert', 'Rousseau', 'Girard', 'Roux', 'Vincent', 'Lefevre', 'Boyer', 'Lopez', 'Bonnet',
    'Andre', 'Francois', 'Mercier', 'Muller', 'Guerin', 'Legrand', 'Sanchez', 'Garnier', 'Chevalier', 'Faure',
    'Perez', 'Clement', 'Fernandez', 'Blanc', 'Robin', 'Morin', 'Gauthier', 'Pereira', 'Perrin', 'Roussel', 'Henry',
    'Duval', 'Gautier', 'Nicolas', 'Masson', 'Marie', 'Noel', 'Ferreira', 'Lemaire', 'Mathieu', 'Riviere', 'Denis',
    'Marchand', 'Rodriguez', 'Dumont', 'Payet', 'Lucas', 'Dufour', 'Dos Santos', 'Joly', 'Blanchard', 'Meunier',
    'Rodrigues', 'Caron', 'Gerard', 'Fernandes', 'Brunet', 'Meyer', 'Barbier', 'Leroux', 'Renard', 'Goncalves',
    'Gaillard', 'Brun', 'Roy', 'Picard', 'Giraud', 'Roger', 'Schmitt', 'Colin', 'Arnaud', 'Vidal', 'Gonzalez',
    'Lemoine', 'Roche', 'Aubert', 'Olivier', 'Leclercq', 'Pierre', 'Philippe', 'Bourgeois', 'Renaud', 'Martins',
    'Leclerc', 'Guillaume', 'Lacroix', 'Lecomte', 'Benoit', 'Fabre', 'Carpentier', 'Vasseur', 'Louis', 'Hubert',
    'Jean', 'Dumas', 'Rolland', 'Grondin', 'Rey', 'Huet', 'Gomez', 'Dupuis', 'Guillot', 'Berger', 'Moulin',
    'Hoarau', 'Menard', 'Deschamps', 'Fleury', 'Adam', 'Boucher', 'Poirier', 'Bertin', 'Charles', 'Aubry',
    'Da Costa', 'Royer', 'Dupuy', 'Maillard', 'Paris', 'Baron', 'Lopes', 'Guyot', 'Carre', 'Jacquet', 'Renault',
    'Herve', 'Charpentier', 'Klein', 'Cousin', 'Collet', 'Leger', 'Ribeiro', 'Hernandez', 'Bailly', 'Schneider',
    'Le Gall', 'Ruiz', 'Langlois', 'Bouvier', 'Gomes', 'Prevost', 'Julien', 'Lebrun', 'Breton', 'Germain', 'Millet',
    'Boulanger', 'Remy', 'Le Roux', 'Daniel', 'Marques', 'Maillot', 'Leblanc', 'Le Goff', 'Barre', 'Perrot',
    'Leveque', 'Marty', 'Benard', 'Monnier', 'Hamon', 'Pelletier', 'Alves', 'Etienne', 'Marchal', 'Poulain',
    'Tessier', 'Lemaitre', 'Guichard', 'Besson', 'Mallet', 'Hoareau', 'Gillet', 'Weber', 'Jacob', 'Collin',
    'Chevallier', 'Perrier', 'Michaud', 'Carlier', 'Delaunay', 'Chauvin', 'Alexandre', 'Marechal', 'Antoine',
    'Lebon', 'Cordier', 'Lejeune', 'Bouchet', 'Pasquier', 'Legros', 'Delattre', 'Humbert', 'De Oliveira', 'Briand',
    'Lamy', 'Launay', 'Gilbert', 'Perret', 'Lesage', 'Gay', 'Nguyen', 'Navarro', 'Besnard', 'Pichon', 'Hebert',
    'Cohen', 'Pons', 'Lebreton', 'Sauvage', 'De Sousa', 'Pineau', 'Albert', 'Jacques', 'Pinto', 'Barthelemy',
    'Turpin', 'Bigot', 'Lelievre', 'Georges', 'Reynaud', 'Ollivier', 'Martel', 'Voisin', 'Leduc', 'Guillet',
    'Vallee', 'Coulon', 'Camus', 'Marin', 'Teixeira', 'Costa', 'Mahe', 'Didier', 'Charrier', 'Gaudin', 'Bodin',
    'Guillou', 'Gregoire', 'Gros', 'Blanchet', 'Buisson', 'Blondel', 'Paul', 'Dijoux', 'Barbe', 'Hardy', 'Laine',
    'Evrard', 'Laporte', 'Rossi', 'Joubert', 'Regnier', 'Tanguy', 'Gimenez', 'Allard', 'Devaux', 'Morvan', 'Levy',
    'Dias', 'Courtois', 'Lenoir', 'Berthelot', 'Pascal', 'Vaillant', 'Guilbert', 'Thibault', 'Moreno', 'Duhamel',
    'Colas', 'Masse', 'Baudry', 'Bruneau', 'Verdier', 'Delorme', 'Blin', 'Guillon', 'Mary', 'Coste', 'Pruvost',
    'Maury', 'Allain', 'Valentin', 'Godard', 'Joseph', 'Brunel', 'Marion', 'Texier', 'Seguin', 'Raynaud', 'Bourdon',
    'Raymond', 'Bonneau', 'Chauvet', 'Maurice', 'Legendre', 'Loiseau', 'Ferrand', 'Toussaint', 'Techer', 'Lombard',
    'Lefort', 'Couturier', 'Bousquet', 'Diaz', 'Riou', 'Clerc', 'Weiss', 'Imbert', 'Jourdan', 'Delahaye', 'Gilles',
    'Guibert', 'Begue', 'Descamps', 'Delmas', 'Peltier', 'Dupre', 'Chartier', 'Martineau', 'Laroche', 'Leconte',
    'Maillet', 'Parent', 'Labbe', 'Potier', 'Bazin', 'Normand', 'Pottier', 'Torres', 'Lagarde', 'Blot', 'Jacquot',
    'Lemonnier', 'Grenier', 'Rocher', 'Bonnin', 'Boutin', 'Fischer', 'Munoz', 'Neveu', 'Lacombe', 'Mendes',
    'Delannoy', 'Auger', 'Wagner', 'Fouquet', 'Mace', 'Ramos', 'Pages', 'Petitjean', 'Chauveau', 'Foucher', 'Peron',
    'Guyon', 'Gallet', 'Rousset', 'Traore', 'Bernier', 'Vallet', 'Letellier', 'Bouvet', 'Hamel', 'Chretien',
    'Faivre', 'Boulay', 'Thierry', 'Samson', 'Ledoux', 'Salmon', 'Gosselin', 'Lecoq', 'Pires', 'Leleu', 'Becker',
    'Diallo', 'Merle', 'Valette'
)

prefixes = ('de', 'de la', 'Le', 'du')
