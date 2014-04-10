class CreateCommunitySubtypes < ActiveRecord::Migration
  def change
    create_table :community_subtypes do |t|
      t.string :name
      t.string :abbr
      t.belongs_to :community_type

      t.timestamps
    end
    add_index :community_subtypes, :community_type_id
  end
end
